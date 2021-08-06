"""scm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from tutorials import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
#router.register(r'posts', views.PostViewSet, basename='post')
urlpatterns = [
    path("api/", include(router.urls)),
    path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),
    #path("api/index/", views.index),
    #path('api/index/', views.IndexPostListAPIView.as_view()),
    #path('tutorials_list/', views.tutorials_list),
    #path('tutorials_detail/<int:pk>/', views.tutorials_detail),
    path('get_test/', views.get_test),
    path('tutorials/', views.TutorialsList.as_view()),
    path('tutorials_detail/<int:pk>/', views.TutorialsDetail.as_view()),
    path('get_info/',views.Get_info.as_view()),

]
