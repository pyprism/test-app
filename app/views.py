from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView

from app.models import Todo, Note
from app.serializers import TodoSerializer, NoteSerializer
# Create your views here.


@api_view(['GET', 'POST'])
def test(request):
    if request.method == 'GET':
        todo = Todo.objects.all()
        if not todo:
            print('blank')
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = TodoSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

