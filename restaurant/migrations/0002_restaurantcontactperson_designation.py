# Generated by Django 3.1.1 on 2020-10-31 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantcontactperson',
            name='designation',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
