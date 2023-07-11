"""
URL configuration for fault_diagnosis_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.index, name="index"),
                  path('index/', views.index),
                  path('upload_diagnosis/', views.upload_diagnosis, name="upload_diagnosis"),
                  path('upload_multi_diagnosis/', views.upload_multi_diagnosis, name="upload_multi_diagnosis"),
                  path('upload_train/', views.upload_train, name="upload_train"),
                  path('diagnosis_tasks_list/', views.diagnosis_tasks_list, name="diagnosis_tasks_list"),
                  path('diagnosis_task_detail/<int:task_id>/', views.diagnosis_task_detail,
                       name='diagnosis_task_detail'),
                  path('train_tasks_list/', views.train_tasks_list, name="train_tasks_list"),
                  path('train_task_detail/<int:task_id>/', views.train_task_detail,
                       name='train_task_detail'),
                  path('login/', views.user_login, name="login"),
                  path('logout/', views.user_logout, name="logout"),
                  path('about/', views.about_page, name="about"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
