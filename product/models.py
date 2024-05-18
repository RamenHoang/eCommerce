from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(max_length=200, null=True)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def object(self):
        for attribute in ['book', 'mobile', 'cloth']:
            try:
                if getattr(self, attribute):
                    return getattr(self, attribute)
            except:
                continue

        return None

    class Meta:
        db_table = "products"
