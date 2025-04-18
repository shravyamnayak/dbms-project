# config.py
import os

class Config:
    SECRET_KEY = os.environ["FLASK_SECRET_KEY"]
    
    # Mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ["MAIL_USERNAME"]
    MAIL_PASSWORD = os.environ["MAIL_PASSWORD"]
    MAIL_DEFAULT_SENDER = MAIL_USERNAME

    # Optional future configs
    # MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")
