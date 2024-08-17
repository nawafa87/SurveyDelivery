import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Survey(db.Model):
    __tablename__ = 'survey'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), nullable=False)
    domains = db.relationship('Domain', backref='survey', lazy=True)

class Domain(db.Model):
    __tablename__ = 'domain'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    admin_email = db.Column(db.String(100), nullable=False)
    email_sent = db.Column(db.Boolean, default=False)
    email_sent_at = db.Column(db.DateTime, default=None)
    email_error_msg = db.Column(db.Text, default=None)
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'), nullable=False)