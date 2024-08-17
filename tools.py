import os
import base64
from flask import current_app, render_template

def get_image_file_as_base64_data(filename):
    filepath = os.path.join(current_app.root_path, 'static', filename)
    with open(filepath, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def render_email_template(survey_url, domain_name):
    try:
        # Encode the logo image
        logo_data = get_image_file_as_base64_data('logo.png')
        
        # Use HTML tags for line breaks
        content = f"""
        <p>Dear Administrator of {domain_name},</p>
        <p>You are invited to complete the survey for your domain.</p>
        """
        
        return render_template('email.html',
                               title="Survey Invitation",
                               subject="You're invited to take a survey",
                               content=content,
                               button_link=survey_url,
                               button_text="Take the Survey",
                               company_name="Survey Corp",
                               company_address="Survey Corp, 123 Survey St, Survey City, 12345 USA",
                               logo_url=f"data:image/png;base64,{logo_data}")
    except Exception as e:
        current_app.logger.error(f"Error rendering email template: {str(e)}")
        raise