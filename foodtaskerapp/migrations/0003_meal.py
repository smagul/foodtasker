# Generated by Django 2.0.7 on 2018-08-06 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0002_customer_driver'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('short_description', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='meal_images')),
                ('price', models.IntegerField(default=0)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meal', to='foodtaskerapp.Restaurant')),
            ],
        ),
    ]
