from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from app.api import TodoResource, NotifyResource

admin.autodiscover()

#todo = TodoResource()
api = Api(api_name='v1')
api.register(TodoResource())
api.register(NotifyResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(api.urls)),
)
