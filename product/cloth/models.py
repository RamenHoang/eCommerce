from django.db import models
from product.models import Product
from product.common.models import Producer


class Style(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "styles"


class Cloth(Product):
    producer = models.ForeignKey(Producer, on_delete=models.SET_NULL, null=True)
    style = models.ForeignKey(Style, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "clothes"
        verbose_name_plural = "Clothes"
