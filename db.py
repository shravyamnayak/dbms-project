# def get_db_connection():
#     return mysql.connector.connect(
#         host="localhost",
#         port=3306,
#         user="admin",
#         password="asdfghjkl",
#         database="doctors_appointment"
#     )

import pymysql
from pymysql.cursors import DictCursor


def get_db_connection():
    return pymysql.connect(
        host='localhost',
        port=3306,
        user='admin',
        password='asdfghjkl',
        database='doctors_appointment',
        cursorclass=DictCursor
    )

import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password=os.environ["MYSQL_PASSWORD"],
        db="doctors_appointment",
        cursorclass=pymysql.cursors.DictCursor
    )
