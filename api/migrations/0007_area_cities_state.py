# Generated by Django 4.1.7 on 2023-04-24 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_trip_detail_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='area_cities',
            name='state',
            field=models.ManyToManyField(to='api.state'),
        ),
    ]
