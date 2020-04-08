from django.contrib.auth import get_user_model
from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework.serializers import CharField, EmailField
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator, ValidationError

User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'password',
        ]


class UserSignupSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2',)
        write_only_fields = ('password1', 'password2',)

    email = EmailField(
        max_length=255,
        validators=[
            UniqueValidator(queryset=User.objects.all()),
        ],
    )
    username = CharField(
        max_length=255,
        validators=[
            UnicodeUsernameValidator(),
        ],
    )
    first_name = CharField(
        max_length=30,
    )
    last_name = CharField(
        max_length=30,
    )
    password1 = CharField(
        min_length=8,
    )
    password2 = CharField(
        min_length=8,
    )

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise ValidationError({'password': 'Passwords do not match'})
        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password2'])
        user.save()
        return user
