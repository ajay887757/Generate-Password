from django.contrib import admin
from django.urls import path,include
from .views import GeneratePassword

urlpatterns = [
    path('GeneratePassword/', GeneratePassword.as_view()),
]