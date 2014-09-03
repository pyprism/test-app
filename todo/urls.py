from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.api import TodoResource

admin.autodiscover()

todo = TodoResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(todo.urls)),
)
