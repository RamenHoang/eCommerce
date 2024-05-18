# Generated by Django 5.0.6 on 2024-05-12 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_order_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_cost',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='subtotal',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]