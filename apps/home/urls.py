# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    path('personas/', views.personas, name='personas'),
    path('new_persona/', views.new_persona, name='new_persona'),
    path('delete_persona/<int:id>/', views.delete_persona, name='delete_persona'),
    path('edit_persona/<int:id>/', views.edit_persona, name='edit_persona'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
