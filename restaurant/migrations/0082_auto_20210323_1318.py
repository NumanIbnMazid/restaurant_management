# Generated by Django 3.1.4 on 2021-03-23 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0081_auto_20210323_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='is_vat_applicable',
            field=models.BooleanField(default=True),
        ),
    ]
