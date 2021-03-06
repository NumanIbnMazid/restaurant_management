# Generated by Django 3.1.1 on 2020-11-17 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0028_table_deleted_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoices', to='restaurant.foodorder'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='payment_status',
            field=models.CharField(choices=[('1_PAID', 'Paid'), ('0_UNPAID', 'Unpaid')], default='0_UNPAID', max_length=25),
        ),
        migrations.AlterField(
            model_name='foodorder',
            name='status',
            field=models.CharField(choices=[('0_ORDER_INITIALIZED', 'Table Scanned'), ('1_ORDER_PLACED', 'User Confirmed'), ('2_ORDER_CONFIRMED', 'In Kitchen'), ('3_IN_TABLE', 'Food Served'), ('4_CREATE_INVOICE', 'Create Invoice'), ('5_PAID', 'Payment Done'), ('6_CANCELLED', 'Cancelled')], default='0_ORDER_INITIALIZED', max_length=120),
        ),
    ]
