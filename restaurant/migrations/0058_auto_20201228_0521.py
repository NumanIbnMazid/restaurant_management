# Generated by Django 3.1.4 on 2020-12-28 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0057_auto_20201227_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='payment_type',
            field=models.ManyToManyField(blank=True, to='restaurant.PaymentType'),
        ),
    ]
