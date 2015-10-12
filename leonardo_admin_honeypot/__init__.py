
from django.apps import AppConfig


default_app_config = 'leonardo_admin_honeypot.Config'


LEONARDO_APPS = ['leonardo_admin_honeypot']

LEONARDO_CONFIG = {
    "ADMIN_HONEYPOT_EMAIL_ADMINS": (True, "Enable sending mails to admins"),
    "ADMIN_HONEYPOT_URL": ("admin-test/", "Path to honeypot admin"),
}
LEONARDO_PUBLIC = True


LEONARDO_PLUGINS = [
    ('leonardo_admin_honeypot.apps.admin_honeypot', 'Admin Honeypot'),
]


class Config(AppConfig):
    name = 'leonardo_admin_honeypot'
    verbose_name = "leonardo-admin-honeypot"
