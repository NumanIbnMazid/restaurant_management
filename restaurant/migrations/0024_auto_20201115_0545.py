# Generated by Django 3.1.1 on 2020-11-15 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0023_foodextratype_deleted_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodextra',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='foodoption',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]