# Generated by Django 5.0.6 on 2024-05-11 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='cloth',
            options={'verbose_name_plural': 'Clothes'},
        ),
        migrations.AlterModelTable(
            name='author',
            table='authors',
        ),
        migrations.AlterModelTable(
            name='book',
            table='books',
        ),
        migrations.AlterModelTable(
            name='category',
            table='categories',
        ),
        migrations.AlterModelTable(
            name='cloth',
            table='clothes',
        ),
        migrations.AlterModelTable(
            name='mobile',
            table='mobiles',
        ),
        migrations.AlterModelTable(
            name='producer',
            table='producers',
        ),
        migrations.AlterModelTable(
            name='product',
            table='products',
        ),
        migrations.AlterModelTable(
            name='publisher',
            table='publishers',
        ),
        migrations.AlterModelTable(
            name='style',
            table='styles',
        ),
        migrations.AlterModelTable(
            name='type',
            table='types',
        ),
    ]
