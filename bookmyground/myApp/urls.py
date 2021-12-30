from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path("", views.index, name='home'),
    path("login", views.loginUser, name='login'),
    path("sign-up", views.signupUser, name='sign-up'),
    # path("logout", views.logoutUser, name='logout')
]