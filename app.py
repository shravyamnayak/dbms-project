import os
import datetime
from flask import Flask, jsonify, render_template, request, redirect, url_for, flash, session
from flask_cors import CORS
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
from db import get_db_connection
from dotenv import load_dotenv
from config import Config
import pymysql

# Import the login_required decorator
from utils import login_required

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.from_object(Config)
CORS(app)
mail = Mail(app)

# Session security
app.permanent_session_lifetime = datetime.timedelta(days=1)

# ✅ Jinja Filters
@app.template_filter('format_date')
def format_date(date):
    if date:
        return date.strftime('%Y-%m-%d')
    return ""

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

# ✅ Utility Functions
def get_all_doctors():
    conn = get_db_connection()
    if not conn:
        flash("Failed to connect to the database", "error")
        return []
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM Doctor")
        doctors = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return doctors

def get_all_patients():
    conn = get_db_connection()
    if not conn:
        flash("Failed to connect to the database", "error")
        return []
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM Patient")
        patients = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return patients

def get_appointments():
    conn = get_db_connection()
    if not conn:
        flash("Failed to connect to the database", "error")
        return []
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = """
            SELECT a.*, p.name as patient_name, d.name as doctor_name 
            FROM Appointment a
            JOIN Patient p ON a.patient_id = p.patient_id
            JOIN Doctor d ON a.doctor_id = d.doctor_id
        """
        cursor.execute(query)
        appointments = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return appointments

# ✅ Routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/doctors")
@login_required(roles=['admin', 'doctor', 'patient'])
def doctors():
    return render_template("doctors.html", doctors=get_all_doctors())

@app.route("/patients")
@login_required(roles=['admin', 'doctor'])
def patients():
    return render_template("patients.html", patients=get_all_patients())

@app.route("/appointments", methods=["GET", "POST"])
@login_required(roles=['admin', 'doctor', 'patient'])
def appointments():
    if request.method == "POST":
        try:
            patient_id = int(request.form['patient_id'])
            doctor_id = int(request.form['doctor_id'])
            date = request.form['date']
            time_str = request.form['time']
            patient_email = request.form['email']

            if len(time_str.split(':')) == 2:
                time_obj = datetime.datetime.strptime(time_str, "%H:%M").time()
            else:
                time_obj = datetime.datetime.strptime(time_str, "%H:%M:%S").time()

            conn = get_db_connection()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT MAX(appointment_id) AS max_id FROM Appointment")
            result = cursor.fetchone()
            new_id = (result['max_id'] or 0) + 1

            cursor.execute(
                "INSERT INTO Appointment (appointment_id, patient_id, doctor_id, date, time, status) VALUES (%s, %s, %s, %s, %s, %s)",
                (new_id, patient_id, doctor_id, date, time_obj, "Scheduled")
            )
            conn.commit()

            cursor.execute("SELECT name FROM Doctor WHERE doctor_id = %s", (doctor_id,))
            doctor_name = cursor.fetchone()['name']

            mail.send(Message(
                subject="Appointment Confirmation",
                recipients=[patient_email],
                body=f"Hello,\n\nYour appointment with Dr. {doctor_name} is scheduled on {date} at {time_str}.\n\nThank you!"
            ))

            flash("Appointment scheduled and confirmation email sent!", "success")
        except Exception as e:
            flash(f"Error: {e}", "error")
        finally:
            cursor.close()
            conn.close()
        return redirect(url_for('appointments'))

    return render_template("appointments.html",
                           doctors=get_all_doctors(),
                           patients=get_all_patients(),
                           appointments=get_appointments())

@app.route("/reschedule/<int:appointment_id>", methods=["POST"])
@login_required(roles=['admin', 'doctor'])
def reschedule_appointment(appointment_id):
    new_date = request.form['new_date']
    new_time = request.form['new_time']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Appointment SET date = %s, time = %s, status = %s WHERE appointment_id = %s",
                   (new_date, new_time, 'Pending', appointment_id))
    conn.commit()
    cursor.close()
    conn.close()

    flash('Appointment successfully rescheduled.', 'success')
    return redirect(url_for('appointments'))

@app.route("/cancel/<int:appointment_id>", methods=["POST"])
@login_required(roles=['admin', 'doctor'])
def cancel_appointment(appointment_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Appointment SET status = %s WHERE appointment_id = %s",
                   ('Cancelled', appointment_id))
    conn.commit()
    cursor.close()
    conn.close()

    flash('Appointment cancelled.', 'warning')
    return redirect(url_for('appointments'))

@app.route("/mark_status/<int:appointment_id>", methods=["POST"])
@login_required(roles=['admin', 'doctor'])
def mark_status(appointment_id):
    new_status = request.form['status']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Appointment SET status = %s WHERE appointment_id = %s",
                   (new_status, appointment_id))
    conn.commit()
    cursor.close()
    conn.close()

    flash(f'Appointment marked as {new_status}.', 'info')
    return redirect(url_for('appointments'))

@app.route("/add_patient", methods=["GET", "POST"])
@login_required(roles=['admin', 'doctor'])
def add_patient():
    if request.method == "POST":
        name, email = request.form['name'], request.form['email']
        user_id = session['user_id']
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO Patient (user_id, name, email) VALUES (%s, %s, %s)", (user_id, name, email))
            conn.commit()
            flash("Patient added!", "success")
            return redirect(url_for('patients'))
        except Exception as e:
            flash(f"Failed to add patient: {e}", "error")
        finally:
            cursor.close()
            conn.close()
    return render_template("add_patient.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name, email, message = request.form.get('name'), request.form.get('email'), request.form.get('message')
        try:
            msg = Message(
                subject=f"Contact Form: {name}",
                sender=email,
                recipients=[os.getenv("MAIL_USERNAME", "shravyamnayak@gmail.com")],
                body=f"Name: {name}\nEmail: {email}\nMessage:\n{message}"
            )
            mail.send(msg)
            flash("Message sent successfully!", "success")
        except Exception as e:
            flash(f"Failed to send message: {e}", "error")
        return redirect(url_for('contact'))
    return render_template("contact.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        conn = get_db_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['role'] = user['role'].lower()  # ✅ Ensure lowercase
            flash("Login successful!", "success")
            return redirect(url_for('index'))
        flash("Invalid credentials.", "error")
        cursor.close()
        conn.close()
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        role = request.form["role"].lower()  # ✅ Store in lowercase

        hashed_password = generate_password_hash(password)

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO users (username, email, password, role, created_at, updated_at, is_active)
                VALUES (%s, %s, %s, %s, NOW(), NOW(), 1)
            """, (username, email, hashed_password, role))
            conn.commit()
            flash("Signup successful! Please login.", "success")
            return redirect(url_for('login'))
        except Exception as e:
            flash(f"Signup failed: {e}", "error")
        finally:
            cursor.close()
            conn.close()
    return render_template("signup.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully.", "success")
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
