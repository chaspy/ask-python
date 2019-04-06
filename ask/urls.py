from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('question/', views.QuestionView.as_view(), name='question'),
    path('question/<int:pk>/', views.DetailView.as_view(), name='detail'),
]