from django.utils.timezone import now
from rest_framework import (
    permissions,
    viewsets,
    serializers,
    views,
    response,
    status,
)

from .models import Post, PostLike
from .serializers import PostSerializer, PostUpdateSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise serializers.ValidationError('Only owner can destroy post')
        instance.delete()

    def perform_update(self, serializer):
        if self.get_object().user != self.request.user:
            raise serializers.ValidationError('Only owner can update post')
        serializer.save()

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return PostUpdateSerializer
        return PostSerializer


class PostLikeUnlikeView(views.APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def post(self, request, *args, **kwargs):
        try:
            post = Post.objects.get(pk=kwargs.get('post_pk'))
        except Post.DoesNotExist:
            return response.Response({'error': 'Post with this pk does not exist'}, status=status.HTTP_404_NOT_FOUND)

        user = request.user

        try:
            post_like = PostLike.objects.get(post=post, user=user)
            post_like.delete()
            return response.Response({'message': 'Unliked'}, status=status.HTTP_200_OK)
        except PostLike.DoesNotExist:
            PostLike.objects.create(post=post, user=user, timestamp=now())
            return response.Response({'message': 'Liked', }, status=status.HTTP_200_OK)
