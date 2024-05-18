from django.db import models
from product.common.models import Producer
from product.models import Product


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "types"


class Mobile(Product):
    producer = models.ForeignKey(Producer, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "mobiles"
