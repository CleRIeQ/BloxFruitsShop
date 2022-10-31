
from django.views.generic import ListView
from .models import itemsForSell


class ShopPageView(ListView):
    model = itemsForSell
    template_name = "shop_page.html"
    context_object_name = "menus"

    def get_context_data(self, **kwargs):
        fruits = itemsForSell.objects.order_by('price')

        context = super().get_context_data(**kwargs)
        context['fruits'] = fruits
        return context