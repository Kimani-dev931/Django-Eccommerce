# Generated by Django 4.1.7 on 2023-03-06 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecoweb', '0005_item_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
