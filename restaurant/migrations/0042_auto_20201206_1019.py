# Generated by Django 3.1.1 on 2020-12-06 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_management', '0023_auto_20201206_0711'),
        ('restaurant', '0041_foodorder_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodorder',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='food_orders', to='account_management.customerinfo'),
        ),
    ]
