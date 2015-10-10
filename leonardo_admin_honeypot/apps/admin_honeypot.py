import django

from django.conf.urls import include, url
from constance import config
from .. import views

from ..urls import urlpatterns


urlpatterns += [
    url(r'^.*$', views.AdminHoneypot.as_view(), name='index')
]