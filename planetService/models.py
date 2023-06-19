from django.db import models

class BaseObject(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)

    class Meta:
        abstract = True

class SpaceBody(BaseObject):
    temperature = models.FloatField()
    rotation_speed = models.FloatField()
    diameter = models.FloatField()
    mass = models.FloatField()
    location = models.TextField()
    type = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True

class Star(SpaceBody):
    age = models.IntegerField()
    distance_to_earth = models.IntegerField()

    class Meta:
        db_table = 'star'


class SalesObject(models.Model):
    color = models.CharField(max_length=7, default='#a9a9a9')

    class Meta:
        abstract = True


class Planet(SpaceBody, SalesObject):
    star = models.ForeignKey('Star', on_delete=models.CASCADE, null=True)
    parent = models.ForeignKey('Planet', on_delete=models.CASCADE, null=True)
    plots_count = models.IntegerField()
    distance_to_parent = models.FloatField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    surface_area = models.FloatField(null=True)
    potential_for_life_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    infrastructure_information = models.TextField(blank=True)

    class Meta:
        db_table = 'planet'


class Plot(BaseObject, SalesObject):
    planet = models.ForeignKey('Planet', on_delete=models.CASCADE, null=False)
    area = models.FloatField(null=True)
    owner = models.ForeignKey('userService.User', on_delete=models.CASCADE, null=True)
    price = models.IntegerField(null=True, default=0)
    markUp = models.IntegerField(default=0)
    location = models.TextField(blank=True)
    mesh = models.JSONField(null=False)
    isSale = models.BooleanField(default=True)

    class Meta:
        db_table = 'plot'

    @property
    def cost(self):
        price = self.price
        mark_up = self.markUp
        cost = price + mark_up
        return cost

    @classmethod
    def update_or_create_plot(self, name, **kwargs):
        defaults = kwargs
        obj, created = self.objects.update_or_create(name=name, defaults=defaults)
        return obj, created
