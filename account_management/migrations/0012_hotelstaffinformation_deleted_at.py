# Generated by Django 3.1.1 on 2020-11-16 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_management', '0011_auto_20201111_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelstaffinformation',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
