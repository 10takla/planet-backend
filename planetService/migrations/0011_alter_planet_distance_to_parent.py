# Generated by Django 3.2.18 on 2023-06-17 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planetService', '0010_auto_20230617_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planet',
            name='distance_to_parent',
            field=models.FloatField(),
        ),
    ]
