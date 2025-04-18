import os
from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
from flask_cors import CORS
from flask_mail import Mail, Message
from db import get_db_connection
import datetime

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "default_secret_key")
CORS(app)

# ✅ Flask-Mail Configuration (Use environment variables for credentials)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get("MAIL_USERNAME", "shravyamnayak@gmail.com")
app.config['MAIL_PASSWORD'] = os.environ.get("MAIL_PASSWORD", "ynlbbubcmkfbjebp")  # Use Gmail App Password
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get("MAIL_USERNAME", "shravyamnayak@gmail.com")

mail = Mail(app)

# ✅ Jinja filter to format date objects
@app.template_filter('format_date')
def format_date(date):
    if date:
        return date.strftime('%Y-%m-%d')
    return ""

# ✅ Jinja filter to format time objects
@app.template_filter('format_time')
def format_time(time):
    if isinstance(time, datetime.time):
        return time.strftime('%H:%M')
    elif isinstance(time, datetime.timedelta):
        total_seconds = int(time.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        return f"{hours:02d}:{minutes:02d}"
    return ""

def get_all_doctors():
    conn = get_db_connection()
    if not conn:
        flash("Failed to connect to the database", "error")
        return []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Doctor")
        doctors = cursor.fetchall()
        cursor.close()
    finally:
        conn.close()
    return doctors

def get_all_patients():
    conn = get_db_connection()
    if not conn:
        flash("Failed to connect to the database", "error")
        return []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Patient")
        patients = cursor.fetchall()
        cursor.close()
    finally:
        conn.close()
    return patients

def get_appointments():
    conn = get_db_connection()
    if not conn:
        flash("Failed to connect to the database", "error")
        return []
    try:
        cursor = conn.cursor()
        query = """
            SELECT a.*, p.name as patient_name, d.name as doctor_name 
            FROM Appointment a
            JOIN Patient p ON a.patient_id = p.patient_id
            JOIN Doctor d ON a.doctor_id = d.doctor_id
        """
        cursor.execute(query)
        appointments = cursor.fetchall()
        cursor.close()
    finally:
        conn.close()
    return appointments

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/doctors", methods=["GET"])
def doctors():
    doctors_list = get_all_doctors()
    return render_template("doctors.html", doctors=doctors_list)

@app.route("/appointments", methods=["GET", "POST"])
def appointments():
    if request.method == "POST":
        try:
            # ✅ Step 1: Collect form data
            patient_id = int(request.form['patient_id'])
            doctor_id = int(request.form['doctor_id'])
            date = request.form['date']
            time = request.form['time']
            patient_email = request.form['email']

            # ✅ Step 2: Insert into DB
            conn = get_db_connection()
            if not conn:
                flash("Failed to connect to the database", "error")
                return redirect(url_for('appointments'))

            cursor = conn.cursor()

            cursor.execute("SELECT MAX(appointment_id) AS max_id FROM Appointment")
            result = cursor.fetchone()
            max_id = result['max_id'] if result and result['max_id'] is not None else 0
            new_id = max_id + 1

            insert_query = """
                INSERT INTO Appointment (appointment_id, patient_id, doctor_id, date, time, status)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (new_id, patient_id, doctor_id, date, time, "Scheduled"))
            conn.commit()

            # ✅ Step 3: Fetch doctor’s name
            cursor.execute("SELECT name FROM Doctor WHERE doctor_id = %s", (doctor_id,))
            doctor_row = cursor.fetchone()
            doctor_name = doctor_row['name'] if doctor_row else "the assigned doctor"

            cursor.close()
            conn.close()

            # ✅ Step 4: Send confirmation email
            msg = Message(
                subject="Appointment Confirmation",
                recipients=[patient_email],
                body=f"""Hello,

Your appointment with Dr. {doctor_name} has been successfully scheduled.

📅 Date: {date}
⏰ Time: {time}

Thank you for choosing XYZ Hospital!
"""
            )
            mail.send(msg)

            # ✅ Step 5: Flash message
            flash("Appointment scheduled successfully and confirmation email sent!", "success")
            return redirect(url_for('appointments'))

        except Exception as e:
            flash(f"Error scheduling appointment: {str(e)}", "error")
            return redirect(url_for('appointments'))

    # ✅ GET: Load data
    doctors_list = get_all_doctors()
    patients_list = get_all_patients()
    appointments_list = get_appointments()
    return render_template("appointments.html", doctors=doctors_list, patients=patients_list, appointments=appointments_list)

@app.route("/patients", methods=["GET"])
def patients():
    patients_list = get_all_patients()
    return render_template("patients.html", patients=patients_list)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        try:
            # ✅ Send email to admin/support (or yourself)
            msg = Message(
                subject=f"New Contact Form Submission from {name}",
                sender=email,
                recipients=[os.environ.get("MAIL_USERNAME", "shravyamnayak@gmail.com")],  # Your email
                body=f"""
                You've received a new message from the contact form:

                Name: {name}
                Email: {email}
                Message: {message}
                """
            )
            mail.send(msg)

            flash("Thank you for your message! We'll get back to you soon.", "success")
        except Exception as e:
            # Capture more detailed error information
            app.logger.error(f"An error occurred while sending the email: {str(e)}")
            flash(f"An error occurred while sending your message: {str(e)}", "error")

        return redirect(url_for('contact'))

    return render_template('contact.html')


@app.route("/api/doctors", methods=["GET"])
def api_doctors():
    doctors_list = get_all_doctors()
    return jsonify(doctors_list)

@app.route("/api/patients", methods=["GET"])
def api_patients():
    patients_list = get_all_patients()
    return jsonify(patients_list)

@app.route("/api/appointments", methods=["GET"])
def api_appointments():
    appointments_list = get_appointments()
    return jsonify(appointments_list)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
