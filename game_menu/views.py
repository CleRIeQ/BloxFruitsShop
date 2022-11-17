
from django.views.generic import ListView
from .models import ItemsForSell, Category


class ShopPageView(ListView):
    model = ItemsForSell
    template_name = "shop_page.html"
    context_object_name = "menus"

    def get_context_data(self, **kwargs):
        fruits = ItemsForSell.objects.order_by('price')
        cats = Category.objects.all()

        context = super().get_context_data(**kwargs)
        context['fruits'] = fruits
        context['cats'] = cats
        return context


class ItemsCategoryView(ListView):
    model = ItemsForSell
    template_name = 'category.html'
    context_object_name = 'fruits'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ItemsCategoryView, self).get_context_data(**kwargs)

        cats = Category.objects.all

        context['cats'] = cats

        return context

    def get_queryset(self):
        slug = self.kwargs['slug']
        return ItemsForSell.objects.filter(category__slug=slug)