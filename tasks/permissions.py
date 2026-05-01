from rest_framework import permissions

class IsProjectMemberForTask(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'admin':
            return True
        return True

    def has_object_permission(self, request, view, obj):
        return request.user in obj.project.members.all()
