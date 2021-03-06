# Generated by Django 2.0.7 on 2018-08-14 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0006_auto_20180808_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='location',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_details', to='foodtaskerapp.Order'),
        ),
    ]
