# Generated by Django 2.0.7 on 2018-08-06 13:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0003_meal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('total', models.IntegerField()),
                ('status', models.IntegerField(choices=[(1, 'Cooking'), (2, 'Ready'), (3, 'On the way'), (4, 'Delivered')])),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('picked_at', models.DateTimeField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=None, to='foodtaskerapp.Customer')),
                ('driver', models.ForeignKey(on_delete=None, to='foodtaskerapp.Driver')),
                ('restaurant', models.ForeignKey(on_delete=None, to='foodtaskerapp.Restaurant')),
            ],
        ),
        migrations.AlterField(
            model_name='meal',
            name='restaurant',
            field=models.ForeignKey(on_delete=None, to='foodtaskerapp.Restaurant'),
        ),
    ]
