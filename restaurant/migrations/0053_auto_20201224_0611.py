# Generated by Django 3.1.1 on 2020-12-24 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0052_restaurantmessages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='order_counter',
            field=models.IntegerField(default=0),
        ),
    ]
