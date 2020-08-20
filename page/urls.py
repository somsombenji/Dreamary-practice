from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('introduce/', views.introduce, name="introduce"),
    path('detail/<int:designer_id>/', views.detail, name="detail"),
]