import django

from django.conf.urls import include, url
from constance import config
from . import views


urlpatterns = []

# Add /admin/login/ as a separate named view in Django 1.7+
if django.VERSION >= (1, 7):
    urlpatterns += [
        url(r'^%slogin/$' % config.ADMIN_HONEYPOT_URL, views.AdminHoneypot.as_view(), name='login')
    ]

urlpatterns += [
    url(r'^%s.*$' % config.ADMIN_HONEYPOT_URL, views.AdminHoneypot.as_view(), name='index')
]