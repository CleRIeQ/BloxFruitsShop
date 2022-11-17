from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    parent = models.ForeignKey('self', related_name="sub_cats", on_delete=models.SET_NULL, blank=True, null=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class ItemsForSell(models.Model):
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=15)
    image = models.ImageField(upload_to='images/', max_length=100)
    is_on_sale = models.BooleanField(default=False)
    category = models.ManyToManyField(Category, verbose_name='категория')

    def __str__(self):
        return self.name


# Create your models here.
