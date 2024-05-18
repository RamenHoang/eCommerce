from django.db import models
from product.models import Product


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "authors"


class Publisher(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "publishers"


class Category(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "categories"
        verbose_name_plural = "Categories"


class Book(Product):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "books"
