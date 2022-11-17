from django.urls import path, include
from .views import send_reset_password_email

urlpatterns = [
    path('', include('allauth.urls')),
]