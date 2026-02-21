from django.shortcuts import render

from rest_framework import generics, status, viewsets 
from rest_framework.response import Response 
from rest_framework.authtoken.models import Token 
from rest_framework import generics, status, viewsets, permissions
from rest_framework.decorators import action 
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer 
from django.contrib.auth import get_user_model 
from .models import CustomUser


CustomUser = get_user_model() 

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer 
    permission_classes = [permissions.AllowAny] 


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

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
    permission_classes = [permissions.IsAuthenticated]  

    def get_object(self):
        return self.request.user 

class UserViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated] 

    @action(detail=True, methods=['post']) 
    def follow(self, request, pk=None):
        user_to_follow = CustomUser.objects.get(pk=pk) 
        if user_to_follow == request.user:
            return Response({'error': 'Cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(user_to_follow)
        return Response({'status': f'You are now followin {user_to_follow.username}'}) 
    
    @action(detail=True, methods=['post'])
    def unfollow(self, request, pk=None):
        user_to_unfollow = CustomUser.objects.get(pk=pk) 
        request.user.following.remove(user_to_unfollow)
        return Response ({'status': f'You have unfollowed {user_to_unfollow.username}'})  