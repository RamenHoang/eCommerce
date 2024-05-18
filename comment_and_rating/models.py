from django.db import models
from product.models import Product
from user.models import User

# Create your models here.

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(default=0, null=True)
    comment = models.TextField(null=True, default="")
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.product.name + " - " + self.user.fullname.__str__()

    class Meta:
        db_table = "reviews"
        verbose_name_plural = "Reviews"
