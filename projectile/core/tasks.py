from __future__ import absolute_import

import logging
logger = logging.getLogger(__name__)

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from celery import shared_task


@shared_task
def send_email(context, template, emails, subject):
    html_body = render_to_string(template, context)
    for email in emails:
        msg = EmailMultiAlternatives(subject=subject, to=[email])
        msg.attach_alternative(html_body, "text/html")
        msg.send()
        logger.info(u"Email sent... <Email: {}, Subject: {}>".format(emails, subject))
