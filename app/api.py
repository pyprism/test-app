import datetime
from .models import Todo
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication


class ExtraPostResource(object):
    """
    For Postman REST client
    """
    def deserialize(self, request, data, format=None):
        if not format:
            format = request.META.get('CONTENT_TYPE', 'application/json')

        if format == 'application/x-www-form-urlencoded':
            return request.POST

        if format.startswith('multipart'):
            multipart_data = request.POST.copy()
            multipart_data.update(request.FILES)
            return multipart_data

        return super(ExtraPostResource, self).deserialize(request, data, format)


class TodoResource(ExtraPostResource, ModelResource):
    class Meta:
        queryset = Todo.objects.all()
        resource_name = 'todo'
        authorization = Authorization()
        authentication = Authentication()
        #serializer = Serializer()


class NotifyResource(ModelResource):
    class Meta:
        queryset = Todo.objects.filter(notify=datetime.date.today())
        resource_name = 'notify'