from django.db import models
from django.shortcuts import render
from allauth.account.views import PasswordResetView
from django.dispatch import receiver
from django.conf import settings
from django.http import HttpRequest
from django.middleware.csrf import get_token


@receiver(models.signals.post_save, sender=settings.AUTH_USER_MODEL)
def send_reset_password_email(sender, instance, created, **kwargs):
    if created:
        request = HttpRequest()

        request.method = 'POST'

        if settings.DEBUG:
            request.META['HTTP_HOST'] = '127.0.0.1:8000'
        else:
            request.META['HTTP_HOST'] = 'www.some_site.com'

        request.POST = {
            'email': instance.email,
            'csrfmiddlewaretoken': get_token(HttpRequest())
        }
        PasswordResetView.as_view(request)
