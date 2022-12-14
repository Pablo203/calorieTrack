# Generated by Django 4.1 on 2022-09-12 18:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userMenu', '0004_meallist_date_meals_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meallist',
            name='date',
            field=models.DateField(default=datetime.date(2022, 9, 12)),
        ),
        migrations.AlterField(
            model_name='meals',
            name='date',
            field=models.DateField(default=datetime.date(2022, 9, 12)),
        ),
        migrations.AlterField(
            model_name='userintreface',
            name='eaten',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userintreface',
            name='toEat',
            field=models.IntegerField(default=3500),
        ),
    ]
