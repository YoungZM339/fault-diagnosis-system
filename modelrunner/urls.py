from django.urls import path
from . import views

app_name = 'modelrunner'

urlpatterns = [
    path('train/', views.model_train, name='train'),
    path('detect/', views.model_detect, name='detect'),
    path('val/', views.model_val, name='val'),
    path('test_train/', views.test_train, name='test_train'),
    path('test_detect/', views.test_detect, name='test_detect'),
]
