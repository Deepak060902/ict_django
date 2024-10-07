from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('blog/<str:title>/', views.view_article, name="view_article"),
    
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),


]
