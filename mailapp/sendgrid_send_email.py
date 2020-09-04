import os
import threading

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from spamgenerator.settings import SENDGRID_API_KEY


def send_email(from_email, to_email, content):
    # sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)
    # message = Mail(
    # from_email=from_email,
    # to_emails=to_email,
    # )
    # message.template_id = template_id
    # message.dynamic_template_data = template_data
    # response = sg.send(message)
    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject='Test sending from E2',
        html_content='<strong>{}</strong>'.format(content))
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        return response
    except Exception as e:
        return e

def add_email_to_threading(from_email, to_email, content, timer):
    print('{}--{}'.format(content, timer))
    t = threading.Timer(timer, send_email, args=(from_email, to_email, content,))
    t.start()
