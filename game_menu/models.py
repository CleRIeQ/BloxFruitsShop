from django.db import models


class itemsForSell(models.Model):
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=15)
    image = models.ImageField(upload_to='images/', max_length=100)
    is_on_sale = models.BooleanField(default=False)


# Create your models here.
