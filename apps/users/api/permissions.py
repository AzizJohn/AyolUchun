from rest_framework.permissions import BasePermission

from apps.common.choices import NEW, PHONE_ENTERED, CODE_VERIFIED, AUTH_DONE


class IsNewUser(BasePermission):
    """
    Check if user auth_status is "NEW"
    """
    def has_permission(self, request, view):
        user = request.user
        return bool(user and user.is_authenticated and user.auth_status == NEW)


class IsPhoneEntered(BasePermission):
    """
    Check if user auth_status is "PHONE_ENTERED"
    """
    def has_permission(self, request, view):
        user = request.user
        return bool(user and user.is_authenticated and user.auth_status == PHONE_ENTERED)


class IsCodeVerified(BasePermission):
    """
    Check if user auth_status is "CODE_VERIFIED"
    """
    def has_permission(self, request, view):
        user = request.user
        return bool(user and user.is_authenticated and user.auth_status == CODE_VERIFIED)


class IsAuthDone(BasePermission):
    """
    Check if user auth_status is "AUTH_DONE"
    """
    def has_permission(self, request, view):
        user = request.user
        return bool(user and user.is_authenticated and user.auth_status == AUTH_DONE)
