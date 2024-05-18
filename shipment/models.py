from django.db import models

class Shipment(models.Model):
    name = models.CharField(max_length=200, null=True)
    cost = models.FloatField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "shipments"
        verbose_name_plural = "Shipments"
