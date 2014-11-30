from rest_framework import serializers
from app.models import Todo, Note


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'content', 'added_at', 'updated_at', 'notify')


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('title', 'content', 'added_at', "updated_at")