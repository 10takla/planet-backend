from django.urls import path, include
from .views import viewCreatePlanet
from .views import views
from .views.views import PlanetViewSet, PlotViewSet

urlpatterns = [
    path('', PlanetViewSet.as_view({'get': 'list'}), name='planets-list'),
    path('<int:id_planet>/', PlanetViewSet.as_view({'get': 'retrieve'}), name='planet-detail'),
    path('plots/', PlotViewSet.as_view({'get': 'list'}), name='plots-list'),
    path('<int:id_planet>/plots/', PlotViewSet.as_view({'get': 'list'}), name='plot-list-detail'),
    path('<int:id_planet>/plots/<int:id_plot>/', PlotViewSet.as_view({'get': 'retrieve'})),
    path('plots/<int:id_plot>/', PlotViewSet.as_view({'get': 'retrieve'}), name='plot-detail'),
    path('plots/<int:id_plot>/update/', views.PlotUpdateView.as_view()),
    path('<int:id_planet>/plots/<int:id_plot>/update/', views.PlotUpdateView.as_view()),
    path('plots/create/', viewCreatePlanet.CreatePlots.as_view()),
    path('plots/basket/', PlotViewSet.as_view({'get': 'list'})),
]
