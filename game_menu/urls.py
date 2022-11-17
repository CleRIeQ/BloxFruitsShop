from django.urls import path

from .views import ShopPageView, ItemsCategoryView

urlpatterns = [
    path('', ShopPageView.as_view(), name='main'),
    path('category/<slug>/', ItemsCategoryView.as_view(), name='category')
]