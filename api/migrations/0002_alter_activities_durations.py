# Generated by Django 4.1.7 on 2023-04-18 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='durations',
            field=models.DurationField(),
        ),
    ]