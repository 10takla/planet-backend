# Generated by Django 3.2.18 on 2023-06-16 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('planetService', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='plot',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='plot',
            name='planet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planetService.planet'),
        ),
        migrations.AddField(
            model_name='planet',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planetService.planet'),
        ),
        migrations.AddField(
            model_name='planet',
            name='star',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planetService.star'),
        ),
    ]
