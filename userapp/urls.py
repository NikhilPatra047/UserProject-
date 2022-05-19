from django.urls import path
from userapp import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout")
]
