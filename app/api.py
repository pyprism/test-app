from .models import Todo
from tastypie.resources import ModelResource


class TodoResource(ModelResource):
    class Meta:
        queryset = Todo.objects.all()
        resource_name = 'todo'
