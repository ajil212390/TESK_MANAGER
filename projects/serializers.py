from rest_framework import serializers
from .models import Project
from django.contrib.auth import get_user_model

User = get_user_model()

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'created_by', 'members', 'created_at']
        read_only_fields = ['created_by', 'created_at']
        extra_kwargs = {
            'members': {'required': False, 'allow_empty': True}
        }

    def validate_members(self, value):
        return value
