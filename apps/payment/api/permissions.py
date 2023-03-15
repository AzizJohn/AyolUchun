from rest_framework.permissions import BasePermission


class IsPaymentOwner(BasePermission):
    """
    return True, if request user is a payer of that payment
    """
    def has_object_permission(self, request, view, obj):
        return bool(request.user and obj.payer == request.user)
