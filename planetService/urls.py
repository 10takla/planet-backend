from django.urls import path, include
from .views import viewCreatePlanet
from .views import views
from .views.views import PlanetViewSet, PlotViewSet, StarViewSet

urls_plots = [
    path('', PlotViewSet.as_view({'get': 'list'}), name='plots-list'),
    path('<int:id_plot>/', PlotViewSet.as_view({'get': 'retrieve'}), name='plot-detail'),
    path('<int:id_plot>/update/', views.PlotUpdateView.as_view(), name='plot-update'),
    path('create/', viewCreatePlanet.CreatePlots.as_view(), name='plots-create'),
    path('basket/', views.PlotViewSet.as_view({'get': 'list'})),
]

urls_planets = [
    path('', PlanetViewSet.as_view({'get': 'list'}), name='planets-list'),
    path('<int:id_planet>/', PlanetViewSet.as_view({'get': 'retrieve'}), name='planet-detail'),
    path('plots/', include(urls_plots)),
    path('<int:id_planet>/plots/', include(urls_plots)),
]

urls_stars = [
    path('', StarViewSet.as_view({'get': 'list'}), name='stars-list'),
    path('<int:id_star>/', StarViewSet.as_view({'get': 'retrieve'}), name='star-detail'),
    path('planets/', include(urls_planets)),
    path('<int:id_star>/planets/', include(urls_planets))
]

urlpatterns = [
    path('stars/', include(urls_stars), name='stars'),
    path('planets/', include(urls_planets), name='planets'),
    path('plots/', include(urls_plots), name='plots'),
]
