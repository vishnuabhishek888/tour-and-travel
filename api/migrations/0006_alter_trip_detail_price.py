# Generated by Django 4.1.7 on 2023-04-19 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_trip_detail_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip_detail',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
