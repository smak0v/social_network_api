from django.contrib.auth import get_user_model
from django.utils.timezone import now
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import (
    UserSerializer,
    UserSignupSerializer,
)

User = get_user_model()


class UserLoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super(TokenObtainPairView, self).post(request)
        user = User.objects.get(username=request.data['username'])
        user.last_login = now()
        user.save()
        return response


class UserSignupView(APIView):
    def post(self, request, *args, **kwargs):
        signup_serializer = UserSignupSerializer(data=request.data)

        if not signup_serializer.is_valid():
            return Response(signup_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = signup_serializer.create(signup_serializer.validated_data)

        user_serializer = UserSerializer(user)
        response_data = {
            'user': user_serializer.data,
            'tokens': self.get_tokens_for_user(user),
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

    @staticmethod
    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


class UserActivityInfoView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            user = User.objects.get(pk=kwargs.get('user_pk'))
        except User.DoesNotExist:
            return Response({'error': 'User with this pk does not exist'}, status=status.HTTP_404_NOT_FOUND)

        response = {
            'last_login': user.last_login,
            'last_request': user.last_request,
        }

        return Response(response, status=status.HTTP_200_OK)
