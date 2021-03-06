# Generated by Django 3.1.4 on 2021-01-03 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0063_auto_20210103_0844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='versionupdate',
            name='customer_app_version_no',
        ),
        migrations.RemoveField(
            model_name='versionupdate',
            name='waiter_app_version_no',
        ),
        migrations.AddField(
            model_name='versionupdate',
            name='is_customer_app',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='versionupdate',
            name='is_waiter_app',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='versionupdate',
            name='version_no',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
