#configuration générale
# par exemple centraliser la clé secrete, base de données, mode de débogage etc


import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://fitbuddy:yourpassword@your-db-endpoint.rds.amazonaws.com/fitbuddy_db") #à adapter!

config = Config()
