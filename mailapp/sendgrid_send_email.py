import os

import sendgrid
from sendgrid.helpers.mail import Mail



data = {
    "user":
        {
            "name": "olga",
            "last_name": "sergeeva"
        }
}

def send_email(from_email, to_email, template_id, template_data):

    sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)
    message = Mail(
    from_email=from_email,
    to_emails=to_email,
    )
    message.template_id = template_id
    message.dynamic_template_data = template_data
    response = sg.send(message)

if __name__ == '__main__':
    send_email(from_email='from_template@gmail.com', to_email='your_address@gmail.com', 
           template_id=SENDGRID_TEMPLATE_ID, template_data=data)


# message = Mail(
#     from_email='from_email@example.com',
#     to_emails='to@example.com',
#     subject='Sending with Twilio SendGrid is Fun',
#     html_content='<strong>and easy to do anywhere, even with Python</strong>')
# try:
#     sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
#     response = sg.send(message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print(e.message)