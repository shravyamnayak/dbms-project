from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
from flask_cors import CORS
from db import get_db_connection
import datetime

app = Flask(__name__)
app.secret_key = "your_secret_key_here"
CORS(app)

# Jinja filter to format date objects


@app.template_filter('format_date')
def format_date(date):
    """Format a date object to YYYY-MM-DD string."""
    if date:
        return date.strftime('%Y-%m-%d')
    return ""

# Jinja filter to format time objects


@app.template_filter('format_time')
def format_time(time):
    """Format a time object to HH:MM string."""
    if isinstance(time, datetime.time):
        return time.strftime('%H:%M')
    elif isinstance(time, datetime.timedelta):
        # Convert timedelta to a formatted string (HH:MM)
        total_seconds = int(time.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        return f"{hours:02d}:{minutes:02d}"
    return ""


def get_all_doctors():
    conn = get_db_connection()
    cursor = conn.cursor()  # Ensure cursor returns dictionaries
    cursor.execute("SELECT * FROM Doctor")
    doctors = cursor.fetchall()
    cursor.close()
    conn.close()
    return doctors


def get_all_patients():
    conn = get_db_connection()
    cursor = conn.cursor()  # Ensure cursor returns dictionaries
    cursor.execute("SELECT * FROM Patient")
    patients = cursor.fetchall()
    cursor.close()
    conn.close()
    return patients


def get_appointments():
    conn = get_db_connection()
    cursor = conn.cursor()  # Ensure cursor returns dictionaries
    query = """
        SELECT a.*, p.name as patient_name, d.name as doctor_name 
        FROM Appointment a
        JOIN Patient p ON a.patient_id = p.patient_id
        JOIN Doctor d ON a.doctor_id = d.doctor_id
    """
    cursor.execute(query)
    appointments = cursor.fetchall()
    cursor.close()
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
            patient_id = int(request.form['patient_id'])
            doctor_id = int(request.form['doctor_id'])
            date = request.form['date']
            time = request.form['time']

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT MAX(appointment_id) AS max_id FROM Appointment")
            result = cursor.fetchone()
            max_id = result['max_id'] if result and result['max_id'] is not None else 0
            new_id = max_id + 1

            insert_query = """
                INSERT INTO Appointment (appointment_id, patient_id, doctor_id, date, time, status)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (new_id, patient_id,
                           doctor_id, date, time, "Scheduled"))

            conn.commit()
            cursor.close()
            conn.close()

            flash("Appointment scheduled successfully!", "success")
            return redirect(url_for('appointments'))

        except Exception as e:
            flash(f"Error scheduling appointment: {str(e)}", "error")
            return redirect(url_for('appointments'))

    doctors_list = get_all_doctors()
    patients_list = get_all_patients()
    appointments_list = get_appointments()

    return render_template(
        "appointments.html",
        doctors=doctors_list,
        patients=patients_list,
        appointments=appointments_list
    )


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

        # Here you would typically save the contact form data or send an email
        # But for now, we'll just flash a success message

        flash("Thank you for your message! We'll get back to you soon.", "success")
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
