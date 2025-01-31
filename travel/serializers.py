from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class RegisterSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password_confirm')

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError('Passwords do not match')
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
