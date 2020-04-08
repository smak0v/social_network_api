from django.urls import path, include
from rest_framework import routers

from .api_views import PostViewSet, PostLikeUnlikeView

router = routers.DefaultRouter()

router.register(r'', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('like/<int:post_pk>/', PostLikeUnlikeView.as_view(), name='post_like_unlike'),
]
