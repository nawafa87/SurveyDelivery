# Survey Delivery System

## Overview
The Survey Delivery System is a Flask-based web application designed to automate the process of sending survey links to domain administrators. It uses a PostgreSQL database for data storage, Redis for task queuing, and MailHog for email testing in development.

## Features
- RESTful API for creating surveys and managing domain information
- Automated email delivery to domain administrators
- Background job processing for email sending
- Docker support for easy deployment and development
- Email templating with custom logos
- Logging of email delivery status

## Project Structure
```
survey-delivery-system/
│
├── app.py                 # Main application entry point
├── config.py              # Configuration settings
├── controllers.py         # Business logic for survey operations
├── docker-compose.yml     # Docker composition file
├── Dockerfile             # Docker build instructions
├── models.py              # Database models
├── requirements.txt       # Python dependencies
├── tasks.py               # Background tasks for email processing
├── tools.py               # Utility functions for email rendering
├── views.py               # API route definitions
├── worker.py              # RQ worker for processing background jobs
│
├── static/
│   └── logo.png           # Logo image for emails
│
└── templates/
    └── email.html         # Email template
```

## Installation and Setup

### Prerequisites
- Docker and Docker Compose

### Steps
1. Clone the repository:
   ```
   git clone <repository-url>
   cd survey-delivery-system
   ```

2. Build and run the Docker containers:
   ```
   docker-compose up --build
   ```

This will start the following services:
- Web application (Flask) on port 5001
- PostgreSQL database
- Redis
- MailHog (SMTP server for development) on ports 1025 (SMTP) and 8025 (Web UI)
- Background worker for processing tasks

## Configuration
The application uses environment variables for configuration. These are set in the `docker-compose.yml` file and can be overridden by creating a `.env` file in the project root.

Key configuration options:
- `FLASK_ENV`: Set to `development` by default
- `DATABASE_URL`: PostgreSQL connection string
- `REDIS_URL`: Redis connection string
- `MAIL_SERVER`, `MAIL_PORT`, etc.: Email server configuration

## Usage

### API Endpoints

1. Create a new survey:
   ```
   POST /create-survey
   Content-Type: application/json

   {
     "survey_url": "https://example.com/survey",
     "domains": [
       {
         "domain_name": "example.com",
         "admin_email": "admin@example.com"
       },
       ...
     ]
   }
   ```

2. Get all surveys:
   ```
   GET /surveys
   ```

3. Get unsent emails:
   ```
   GET /unsent-emails
   ```

### Viewing Emails
In development, you can view sent emails using MailHog's web interface at `http://localhost:8025`.

## Dependencies
- Flask
- Redis
- RQ (Redis Queue)
- Flask-SQLAlchemy
- python-dotenv
- psycopg2-binary
- Flask-Mail

For a complete list with versions, see `requirements.txt`.


