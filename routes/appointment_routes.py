from flask import Blueprint, request, jsonify
from db import get_db_connection

appointment_bp = Blueprint("appointment", __name__)

@appointment_bp.route("/appointments", methods=["GET"])
def get_appointments():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Appointment")
    appointments = cursor.fetchall()
    conn.close()
    return jsonify(appointments)
