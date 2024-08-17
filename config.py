import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:password@localhost/surveydb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')

    # Email (MailHog for development)
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'mailhog')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 1025))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'False').lower() in ('true', 'on', '1')
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'False').lower() in ('true', 'on', '1')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', 'noreply@survey.com')
