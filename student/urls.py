from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    # path('home/',views.home),
    path('home/',views.student_list),
]
