from django.urls import path
from . import views

app_name = 'filemanager'

urlpatterns = [
    path('upload/', views.upload, name='upload'),
]
