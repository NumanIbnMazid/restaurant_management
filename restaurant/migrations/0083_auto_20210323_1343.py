# Generated by Django 3.1.4 on 2021-03-23 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0082_auto_20210323_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='discount_schedule_type',
            field=models.CharField(choices=[('Time_wise', 'Time wise'), ('Date_wise', 'Date wise')], default='Date_wise', max_length=50),
        ),
    ]
