# Generated by Django 5.0.6 on 2024-05-12 08:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_table_alter_orderitem_table'),
        ('user', '0004_alter_address_city_alter_address_no_house_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.address'),
        ),
    ]
