from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        # Name
        model = Task
        # fields = ('id', 'title', 'description', 'done')
        fields = "__all__"
