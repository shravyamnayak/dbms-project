import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="admin",
        password="asdfghjkl",
        database="doctors_appointment"
    )