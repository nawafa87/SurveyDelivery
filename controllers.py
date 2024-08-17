from flask import jsonify
from models import db, Survey, Domain
from rq import Queue
from redis import Redis
from tasks import process_survey

class SurveyController:
    queue = None

    @classmethod
    def initialize(cls, app):
        redis_conn = Redis.from_url(app.config['REDIS_URL'])
        cls.queue = Queue(connection=redis_conn)

    @classmethod
    def create_survey(cls, data):
        survey_url = data.get('survey_url')
        domains_data = data.get('domains', [])

        if not survey_url or not domains_data:
            return jsonify({"error": "survey_url and domains are required"}), 400
        
        survey = Survey(url=survey_url)
        db.session.add(survey)
        db.session.commit()

        for domain_data in domains_data:
            domain = Domain(
                name=domain_data['domain_name'],
                admin_email=domain_data['admin_email'],
                survey_id=survey.id
            )
            db.session.add(domain)
        
        db.session.commit()

        cls.queue.enqueue(process_survey, survey.id)

        return jsonify({"message": "Request Received and Survey Email will be sent", "survey": survey.id}), 202

    @staticmethod
    def get_all_surveys():
        surveys = Survey.query.all()
        surveys_list = []
        
        for survey in surveys:
            survey_data = {
                'id': survey.id,
                'url': survey.url,
                'domains': [
                    {
                        'id': domain.id,
                        'name': domain.name,
                        'admin_email': domain.admin_email,
                        'email_sent': domain.email_sent,
                        'email_sent_at': domain.email_sent_at.isoformat() if domain.email_sent_at else None,
                        'email_error_msg': domain.email_error_msg,
                    } for domain in survey.domains
                ]
            }
            surveys_list.append(survey_data)
        
        return jsonify(surveys_list), 200

    @staticmethod
    def get_unsent_emails():
        unsent_domains = Domain.query.filter_by(email_sent=False).all()
        unsent_list = []
        
        for domain in unsent_domains:
            domain_data = {
                'id': domain.id,
                'name': domain.name,
                'admin_email': domain.admin_email,
                'survey_id': domain.survey_id,
                'survey_url': domain.survey.url if domain.survey else None,
                'email_error_msg': domain.email_error_msg,
            }
            unsent_list.append(domain_data)
        
        return jsonify(unsent_list), 200