# Generated by Django 3.1.1 on 2020-12-30 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0059_versionupdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='versionupdate',
            old_name='is_customer',
            new_name='is_customer_app',
        ),
        migrations.RenameField(
            model_name='versionupdate',
            old_name='is_waiter',
            new_name='is_waiter_app',
        ),
        migrations.RenameField(
            model_name='versionupdate',
            old_name='version_id',
            new_name='version_no',
        ),
    ]
