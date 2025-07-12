import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/skill_swap.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
