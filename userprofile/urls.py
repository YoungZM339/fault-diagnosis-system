from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns = [
    path('user_login/', views.user_login, name='user_login'),
    path('user_register/', views.user_register, name='user_register'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('user_delete/', views.user_delete, name='user_delete'),
    path('user_get_profile/', views.user_get_profile, name='user_get_profile'),
]
