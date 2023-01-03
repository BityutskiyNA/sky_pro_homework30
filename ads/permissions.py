from rest_framework.permissions import BasePermission

from user.models import User


class AdDelPermissions(BasePermission):
    message = "Редактировать объявления может только владелец или администратор"

    def has_object_permission(self, request, view, obj):
        if request.user.role == User.ADMINISTRATOR:
            return True
        if request.user == view.queryset[(view.kwargs['pk'] - 1)].author:
            return True


class AdUpdatePermissions(BasePermission):
    message = "Редактировать объявления может только владелец или администратор"

    def has_object_permission(self, request, view, obj):
        if request.user.role == User.ADMINISTRATOR:
            return True
        if request.user == view.queryset[(view.kwargs['pk'] - 1)].author:
            return True
