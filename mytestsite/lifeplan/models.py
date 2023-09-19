from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    brand = models.CharField(max_length=255)

class Item(models.Model):
    amount = models.IntegerField()
    model_name = models.CharField(max_length=255)
    size = models.IntegerField()
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/")
    order_id = models.ForeignKey('Order',on_delete=models.PROTECT)

class Order(models.Model):
    items_amount = models.IntegerField()
    is_paid = models.BooleanField()
    user_id = models.ForeignKey('User', on_delete=models.PROTECT)

