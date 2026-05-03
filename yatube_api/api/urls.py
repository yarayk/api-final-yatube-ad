from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('groups', GroupViewSet, basename='group')
router.register('follow', FollowViewSet, basename='follow')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('v1/jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('v1/jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),
]
