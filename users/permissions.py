from rest_framework import permissions


class IsUser(permissions.BasePermission):
    def has_object_permission(self, requests, view, obj):
        if obj.author == requests.user:
            return True
        return False


class IsAdmin(permissions.BasePermission):

    def has_permission(self, requests, view):
        if requests.user.role == 'admin':
            return True
        return False
