# Generated by Django 3.1.1 on 2020-11-05 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_management', '0008_remove_hotelstaffinformation_shift_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='email',
            field=models.EmailField(blank=True, max_length=35, null=True),
        ),
    ]
