import logging
from flask import current_app
from models import db, Survey
from flask_mail import Mail, Message
import datetime
from tools import render_email_template

logger = logging.getLogger(__name__)

"""
Background tasks for email processing
Tasks.py is responsible for
Background tasks, Process survey and sending email to Admins.
"""

def send_email(to, subject, html_content):
    try:
        mail = Mail(current_app)
        msg = Message(subject,
                      recipients=[to],
                      html=html_content,
                      sender=current_app.config['MAIL_DEFAULT_SENDER'])
        
        mail.send(msg)
        return True, None
    except Exception as e:
        error_msg = f"Failed to send email: {str(e)}"
        logger.error(error_msg)
        return False, error_msg

def process_survey(survey_id):
    with current_app.app_context():
        survey = Survey.query.get(survey_id)
        if not survey:
            logger.warning(f"Survey with id {survey_id} not found.")
            return

        for domain in survey.domains:
            
            email_content = render_email_template(survey.url, domain.name)
            success, error_msg = send_email(domain.admin_email, "Survey Invitation", email_content)
            
            if success:
                domain.email_sent = True
                domain.email_sent_at = datetime.datetime.now()
                domain.error_msg = None
            else:
                domain.email_sent = False
                domain.email_sent_at = None
                domain.error_msg = error_msg
            
            db.session.commit()

