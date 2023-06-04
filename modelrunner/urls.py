from django.urls import path
from . import views

app_name = 'modelrunner'

urlpatterns = [
    path('train/', views.model_train, name='train'),
    path('detect/', views.model_detect, name='detect'),
    path('val/', views.model_val, name='val'),
    path('test_result/', views.test_result, name='test_result'),
]
