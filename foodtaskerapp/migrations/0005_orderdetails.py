# Generated by Django 2.0.7 on 2018-08-06 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0004_auto_20180806_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('sub_total', models.IntegerField()),
                ('meal', models.ForeignKey(on_delete=None, to='foodtaskerapp.Meal')),
                ('order', models.ForeignKey(on_delete=None, related_name='order_details', to='foodtaskerapp.Order')),
            ],
        ),
    ]