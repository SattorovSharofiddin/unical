from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Shop(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.title


class Category(MPTTModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = ArrayField(models.URLField())
    active = models.BooleanField(default=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products')
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    is_moderator = models.BooleanField(default=False)
