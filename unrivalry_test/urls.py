from django.urls import path, re_path
from unrivalry_test import views

urlpatterns = [
    path('test_api', views.test_api),
]
