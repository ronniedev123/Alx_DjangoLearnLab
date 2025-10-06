from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from .models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'bio', 'profile_picture', 'followers']
        read_only_fields = ['followers', 'id']

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)


    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'bio']


    def create(self, validated_data):
        password = validated_data.pop('password')
        user = get_user_model().objects.create_user(password=password, **validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)


    def validate(self, data):
        user = authenticate(username=data.get('username'), password=data.get('password'))
        if not user:
           raise serializers.ValidationError('Invalid credentials')
        token, _ = Token.objects.get_or_create(user=user)
        return {'username': user.username, 'token': token.key}