# Generated by Django 3.1.1 on 2020-11-03 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_management', '0004_auto_20201102_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
