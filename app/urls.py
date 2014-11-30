__author__ = 'prism'
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'app.views',
    url(r'todo/$', 'test'),
)