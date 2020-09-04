# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from unrivalry_test import views as test_view
from unrivalry import views as main_view

urlpatterns = [

    # The home page
    path('templates', views.index, name='home'),
    path('api', views.ini_api),
    path('test_api', test_view.test_api),
    path('date', views.ini_current_datetime),
    path('', views.web_index),
    path('line_follower', views.web_line_follower),
    path('manipulator', views.web_manipulator),
    path('humanoid', views.web_humanoid),
    path('about_this_page', views.web_about_this_page),
    path('unrivalry_add_person', main_view.unrivalry_add_person),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
