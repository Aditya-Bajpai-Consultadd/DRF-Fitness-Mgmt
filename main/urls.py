from django.urls import path
from . import views
from .views import viewOrAddMembers, updateOrDeleteMembers, register
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('', views.home, name='home'),
    path('members/', viewOrAddMembers, name='viewOrAddMembers'),  
    path('members/<int:member_id>/', updateOrDeleteMembers, name='updateOrDeleteMembers'), 
    path('register/', register, name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  
]