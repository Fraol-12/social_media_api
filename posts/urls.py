from .views import PostViewSet, CommentViewSet, LikePostView, UnlikePostView, FeedView
from django.urls import path
from rest_framework_nested import routers 


router = routers.SimpleRouter() 
router.register(r'', PostViewSet, basename='post')  

posts_router = routers.NestedSimpleRouter(router, r'', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='post-comments')


urlpatterns = router.urls + posts_router.urls + [
    path('feed/', FeedView.as_view(), name='feed'),
    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
]

