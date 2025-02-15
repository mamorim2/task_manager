from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.StringRelatedField()

    class Meta:
        model = Task
        fields = '__all__'