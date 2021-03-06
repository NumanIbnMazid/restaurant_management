# Generated by Django 3.1.1 on 2020-11-11 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_management', '0010_auto_20201105_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='email_address',
        ),
        migrations.CreateModel(
            name='CustomerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(blank=True, max_length=35, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
