from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user and request.user.is_authenticated:
            return True
        else:
            return False
    