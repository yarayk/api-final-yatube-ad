from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import APIView


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: APIView) -> bool:
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(
        self, request: Request, view: APIView, obj: object
    ) -> bool:
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
