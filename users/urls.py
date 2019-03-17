from django.conf.urls import url, include
from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    url('signup/', views.SignUp.as_view(), name="signup")
]
