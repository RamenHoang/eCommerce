import enum

from django.db import models

# Create your models here.
PAYMENT_TYPES = [
    ('card', 'Card'),
    ('cod', 'Cash on Delivery'),
]

class Payment(models.Model):
    name = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, choices=PAYMENT_TYPES, default='card')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "payments"
        verbose_name_plural = "Payments"
