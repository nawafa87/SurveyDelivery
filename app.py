from flask import Flask
from models import db
from config import Config
from flask_mail import Mail
from views import views

"""
Main application entry point
This file is the root of the application.
It is responsible for initializing the Flask app, configuring the database and mail services.
"""

app = Flask(__name__)
app.config.from_object(Config)

#Initialize Database and Mail instance
db.init_app(app)
mail = Mail(app)

#Load views by registering the Blueprint
app.register_blueprint(views)

#Create all tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)