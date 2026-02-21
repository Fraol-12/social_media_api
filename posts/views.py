from django.shortcuts import render

from rest_framework import viewsets, filters, status
from rest_framework import permissions
from rest_framework.response import Response 
from rest_framework.views import APIView 
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend 
from .models import Post, Comment, Like, Notification 
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly 
from django.shortcuts import get_object_or_404 


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all() 
    serializer_class = PostSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter] 
    search_fields = ['title', 'content'] 


    def perform_create(self, serializer):
        serializer.save(author=self.request.user) 

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])  
    def like(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk) 
        like, created = Like.objects.get_or_create(user=request.user, post=post) 

        if created:
            if post.author != request.user:
                Notification.objects.create(
                    recipient=post.author,
                    actor=request.user,
                    verb='liked your post',
                    target=post 
                )
            return Response({'status': f'You liked "{post.title}"'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 'You already liked this post'}, status=status.HTTP_200_OK)

    @action(detail=True,  methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def unlike(self, request, pk=None):
        post = self.get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post).first()
        if like:
            like.delete()
            return Response({'status': f'You unliked "{post.title}"'}, status=status.HTTP_200_OK) 
        else:
            return Response({'status': 'You have not liked this post'}, status=status.HTTP_400_BAD_REQUEST)             

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