from flask import Blueprint, request, jsonify
from db import get_db_connection  # Ensure this import is correct

patient_bp = Blueprint("patient_bp", __name__)

@patient_bp.route("/api/patients", methods=["GET"])
def get_patients():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM patients")  # Ensure 'patients' table exists
    patients = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(patients)