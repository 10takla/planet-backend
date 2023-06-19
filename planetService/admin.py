from django.contrib import admin
from .models import Plot, Planet


# class PlotAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'planet', 'owner', 'area', 'price', 'markUp', 'location',
#                     'description', 'mesh','color','isSale')
#     list_editable = ('name', 'planet', 'area', 'owner', 'price', 'markUp', 'location', 'description',
#                  'mesh', 'color',)
#
#
# admin.site.register(Plot, PlotAdmin)
#
#
# class PlanetAdmin(admin.ModelAdmin):
#     list_display = ( 'id', 'name', 'rating', 'plots_count', 'description', 'type', 'diameter',
#                      'mass', 'number_of_satellites', 'surface_area',
#                      'potential_for_life_percent', 'available_land_area', 'average_land_price',
#         'infrastructure_information', 'location_information', 'additional_features', 'color')
#     list_editable = (
#         'name', 'rating', 'plots_count', 'description', 'type', 'diameter', 'mass',
#         'number_of_satellites','surface_area','potential_for_life_percent',
#         'available_land_area', 'average_land_price', 'infrastructure_information',
#         'location_information', 'additional_features', 'color')
#
#
# admin.site.register(Planet, PlanetAdmin)
