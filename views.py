from flask import Blueprint, request, jsonify
from controllers import SurveyController

"""
API route definitions
Views.py have the route for this app:
- /create-survey(POST)
- /surveys(GET)
- /unsent-emails(GET)
"""

views = Blueprint('views', __name__)

@views.record_once
def on_load(state):
    app = state.app
    SurveyController.initialize(app)

@views.route('/create-survey', methods=['POST'])
def create_survey():
    data = request.json
    return SurveyController.create_survey(data)

@views.route('/surveys', methods=['GET'])
def get_all_surveys():
    return SurveyController.get_all_surveys()

@views.route('/unsent-emails', methods=['GET'])
def get_unsent_emails():
    return SurveyController.get_unsent_emails()


