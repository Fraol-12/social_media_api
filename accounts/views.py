from django.shortcuts import render

from rest_framework import generics, status 
from rest_framework.response import Response 
from rest_framework.authtoken.models import Token 
from rest_framework.permissions import AllowAny, IsAuthenticated 
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer 
from django.contrib.auth import get_user_model 

user = get_user_model() 

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer 
    permission_classes = [AllowAny] 


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data) 
        serializer.is_valid(raise_exception=True) 
        user = serializer.validated_data['user'] 
        token, _=Token.objects.get_or_create(user=user) 

        return Response({
            'token': token.key,
            'username':user.username,

        }, status=status.HTTP_200_OK) 
    
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated] 

    def get_object(self):
        return self.request.user 
    
        