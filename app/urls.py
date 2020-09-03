# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('templates', views.index, name='home'),
    path('api', views.ini_api),
    path('date', views.ini_current_datetime),
    path('', views.web_index),
    path('line_follower', views.web_line_follower),
    path('manipulator', views.web_manipulator),
    path('humanoid', views.web_humanoid),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
