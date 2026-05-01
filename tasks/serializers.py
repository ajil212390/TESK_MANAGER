from rest_framework import serializers
from .models import Task
from projects.models import Project

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'priority', 'due_date', 'project', 'assigned_to', 'created_at', 'updated_at']

    def validate(self, data):
        project = data.get('project')
        assigned_to = data.get('assigned_to')
        
        if assigned_to and project:
            if not project.members.filter(id=assigned_to.id).exists():
                raise serializers.ValidationError({"assigned_to": "Assigned user must be a member of the project."})
                
        return data
