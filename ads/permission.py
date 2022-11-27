from rest_framework.permissions import BasePermission
from users.models import UserRole, User


class AdsPermission(BasePermission):
    message = "Редактирование объявления доступно владельцу, модератору или администратору."

    def has_object_permission(self, request, view, obj):
        if request.user.role == UserRole.ADMIN or request.user.role == UserRole.MODERATOR \
                or request.user == obj.author:
            return True
        return False


class SelectionAuthorPermission(BasePermission):
    message = "Редактирование подборки объявлений разрешено только владельцу"

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user.id:
            return True
        return False
