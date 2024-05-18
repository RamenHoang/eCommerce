from django.db import models


# Create your models here.
class Producer(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "producers"
