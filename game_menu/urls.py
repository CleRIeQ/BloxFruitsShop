from django.urls import path
from .views import ShopPageView

urlpatterns = [
    path('shop/', ShopPageView.as_view()),
]