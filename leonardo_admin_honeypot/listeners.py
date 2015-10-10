from django.conf import settings
from django.core.mail import mail_admins
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from .signals import honeypot


def notify_admins(instance, request, **kwargs):
    context = {
        'request': request,
        'instance': instance,
    }
    subject = render_to_string('admin_honeypot/email_subject.txt', context).strip()
    message = render_to_string('admin_honeypot/email_message.txt', context).strip()
    if getattr(settings, 'ADMIN_HONEYPOT_EMAIL_ADMINS', True):
        mail_admins(subject=subject, message=message)
    raise Exception(message)

honeypot.connect(notify_admins)