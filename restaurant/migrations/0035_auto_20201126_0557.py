# Generated by Django 3.1.1 on 2020-11-26 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0034_discount_restaurant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discount',
            old_name='discount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='discount',
            old_name='discount_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='discount',
            old_name='discount_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='discount',
            old_name='discount_url',
            new_name='url',
        ),
    ]
