# Generated by Django 3.1.4 on 2021-01-02 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_management', '0036_fcmnotificationcustomer'),
    ]

    operations = [
        migrations.AddField(
            model_name='fcmnotificationcustomer',
            name='data',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
