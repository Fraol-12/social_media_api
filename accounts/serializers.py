from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) 

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user     

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField() 

    def validate(self, data):
        user = authenticate(**data)
        if not user:
            raise serializers.ValidationError('Invalid Credentials')
        data['user'] = user 
        return data     

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture']