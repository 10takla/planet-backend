from django.db import models
from django.utils import timezone

class Planet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    plots_count = models.IntegerField()
    description = models.TextField(null=True)
    type = models.CharField(max_length=255, blank=True)
    diameter = models.FloatField(null=True)
    mass = models.FloatField(null=True)
    number_of_satellites = models.IntegerField(null=True)
    surface_area = models.FloatField(null=True)
    potential_for_life_percent = models.BooleanField(default=True)
    available_land_area = models.FloatField(null=True)
    average_land_price = models.IntegerField(null=True)
    infrastructure_information = models.TextField(blank=True)
    location_information = models.TextField(blank=True)
    additional_features = models.TextField(blank=True)
    color = models.CharField(max_length=7, blank=True)

    class Meta:
        db_table = 'planet'


class Plot(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, null=False, max_length=755)
    planet = models.ForeignKey('Planet', on_delete=models.CASCADE, null=False)
    area = models.FloatField(null=True)
    price = models.IntegerField(null=True, default=0)
    markUp = models.IntegerField(default=0)
    location = models.TextField(blank=True)
    description = models.TextField(blank=True)
    available_for_sale = models.BooleanField(default=True)
    mesh = models.JSONField(null=False)
    color = models.CharField(max_length=7, blank=True)
    isSale = models.BooleanField(default=True)

    class Meta:
        db_table = 'plot'

    @classmethod
    def update_or_create_plot(self, name, **kwargs):
        defaults = kwargs
        obj, created = self.objects.update_or_create(name=name, defaults=defaults)
        return obj, created

