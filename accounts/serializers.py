from rest_framework import serializers 
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token 

User = get_user_model().objects.create_user

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) 

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
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