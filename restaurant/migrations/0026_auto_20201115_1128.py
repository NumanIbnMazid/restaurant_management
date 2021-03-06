# Generated by Django 3.1.1 on 2020-11-15 11:28

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0025_auto_20201115_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodorder',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('grand_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('order_info', django.contrib.postgres.fields.jsonb.JSONField()),
                ('updated_at', models.DateField(auto_now=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('restaurant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.restaurant')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
