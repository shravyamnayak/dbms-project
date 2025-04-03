from flask import Blueprint, request, jsonify
from db import get_db_connection

doctor_bp = Blueprint("doctor", __name__)

@doctor_bp.route("/doctors", methods=["GET"])
def get_doctors():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Doctor")
    doctors = cursor.fetchall()
    conn.close()
    return doctors