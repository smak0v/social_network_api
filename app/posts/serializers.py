from rest_framework import serializers

from .models import Post, PostLike


class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    @staticmethod
    def get_likes_count(post):
        return PostLike.objects.filter(post=post).count()


class PostUpdateSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'
        extra_kwargs = {
            'title': {'required': False},
            'description': {'required': False},
            'content': {'required': False},
            'user': {'read_only': True},
            'timestamp': {'read_only': True},
            'likes_count': {'read_only': True},
        }

    @staticmethod
    def get_likes_count(post):
        return PostLike.objects.filter(post=post).count()
