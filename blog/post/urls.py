from django.urls import path, include
from . import *


urlpatterns = [
    path('home/', views.home, name="home"),
    path('view_article/', views.view_article, name="view_article"),
    
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),


]
