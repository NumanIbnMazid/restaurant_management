# Generated by Django 3.1.1 on 2020-11-15 07:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0024_auto_20201115_0545'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodorder',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='foodorder',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='foodorder',
            name='status',
            field=models.CharField(choices=[('0_ORDER_INITIALIZED', 'Table Scanned'), ('1_ORDER_PLACED', 'User Confirmed'), ('2_ORDER_CONFIRMED', 'In Kitchen'), ('3_IN_TABLE', 'Food Served'), ('4_PAID', 'Payment Done'), ('5_CANCELLED', 'Cancelled')], default='0_ORDER_INITIALIZED', max_length=120),
        ),
        migrations.AlterField(
            model_name='ordereditem',
            name='status',
            field=models.CharField(choices=[('0_ORDER_INITIALIZED', 'Table Scanned'), ('1_ORDER_PLACED', 'User Confirmed'), ('2_ORDER_CONFIRMED', 'In Kitchen'), ('3_IN_TABLE', 'Food Served'), ('4_CANCELLED', 'Cancelled')], default='0_ORDER_INITIALIZED', max_length=120),
        ),
    ]