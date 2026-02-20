from django.urls import path, include
from .views import RegisterView, LoginView, ProfileView, UserViewSet 
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns= router.urls 


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),

    path('profile/', ProfileView.as_view()),
  
    path('', include(router.urls)),

]
