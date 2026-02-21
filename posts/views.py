from django.shortcuts import render

from rest_framework import viewsets, filters 
from rest_framework import permissions
from rest_framework.response import Response 
from rest_framework.views import APIView 
from django_filters.rest_framework import DjangoFilterBackend 
from .models import Post, Comment 
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly 



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all() 
    serializer_class = PostSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter] 
    search_fields = ['title', 'content'] 


    def perform_create(self, serializer):
        serializer.save(author=self.request.user) 

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all() 
    serializer_class = CommentSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] 

    def perform_create(self, serializer):
        serializer.save(author=self.request.user) 

class FeedView(APIView):
    Permission_classes = [permissions.IsAuthenticated] 

    def get(self, request):
        user = request.user 
        following_users = user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at') 
        serializer = PostSerializer(posts, many=True) 
        return Response(serializer.data) 