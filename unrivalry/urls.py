from django.urls import path, include, re_path
from unrivalry import views

urlpatterns = [
    path('unrivalry_add_person', views.unrivalry_add_person, name='add_person'),
    re_path(r'^.*\.*', views.unrivalry_pages, name='pages'),
]
