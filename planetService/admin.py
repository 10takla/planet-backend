from django.contrib import admin
from .models import Plot, Planet


class PlotAdmin(admin.ModelAdmin):
    list_display = ('id', 'planet', 'area', 'owner', 'price', 'markUp', 'location', 'mesh', 'isSale',
                    'name', 'description', 'color'
                    )
    list_editable = ('planet', 'area', 'owner', 'price', 'markUp', 'location', 'mesh', 'isSale',
                     'name', 'description', 'color'
                     )


admin.site.register(Plot, PlotAdmin)


class PlanetAdmin(admin.ModelAdmin):
    list_display = ('id', 'star', 'parent', 'plots_count', 'distance_to_parent', 'rating', 'surface_area',
                    'potential_for_life_percent', 'infrastructure_information', 'temperature',
                    'rotation_speed', 'diameter', 'mass', 'location', 'type',
                    'name', 'description', 'color'
                    )
    list_editable = ('star', 'parent', 'plots_count', 'distance_to_parent', 'rating', 'surface_area',
        'potential_for_life_percent', 'infrastructure_information', 'temperature',
        'rotation_speed', 'diameter', 'mass', 'location', 'type',
        'name', 'description', 'color'
    )


admin.site.register(Planet, PlanetAdmin)
