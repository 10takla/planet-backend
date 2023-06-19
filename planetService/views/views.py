from django.db.models import F, Max
from rest_framework import generics
from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from ..models import Planet, Plot
from planetService.serializers import PlanetSerializer, PlotSerializer, PlotUpdateSerializer, Star, StarSerializer


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def list(self, request, *args, **kwargs):
        limit_from = self.request.GET.get('from') or 0
        limit_to = self.request.GET.get('to') or 10
        queryset = self.get_queryset()
        filtered_queryset = self.filter_queryset(queryset)
        paginated_queryset = filtered_queryset[int(limit_from): int(limit_to)]
        serializer = self.get_serializer(paginated_queryset, many=True)
        return Response(serializer.data)

    def get_serializer_context(self):
        format = self.request.accepted_renderer.format if self.request.accepted_renderer else None
        fields = self.request.GET.get('fields')

        context = {
            'request': self.request,
            'format': format,
        }

        if fields:
            context['fields'] = fields.split(',')

        if 'me' in self.request.path and self.request.user.is_authenticated:
            context['for_user'] = True

        return context


class StarViewSet(BaseViewSet):
    queryset = Star.objects.all()
    serializer_class = StarSerializer
    lookup_url_kwarg = 'id_star'

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        data = response.data

        return Response(data)


class PlanetViewSet(BaseViewSet):
    queryset = Planet.objects.order_by('id')
    serializer_class = PlanetSerializer
    lookup_url_kwarg = 'id_planet'

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        data = response.data
        print(data)
        return Response(data)


class PlotViewSet(BaseViewSet):
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
    lookup_url_kwarg = 'id_plot'

    def get_queryset(self):
        queryset = super().get_queryset()
        id_planet = self.kwargs.get('id_planet')
        if id_planet:
            queryset = queryset.filter(planet_id=id_planet)

        user = self.kwargs.get('user')

        if user == 'me':
            if not self.request.user.is_authenticated:
                return queryset.none()
            user = self.request.user

            if 'basket' in self.request.path:
                queryset = queryset.filter(basket__user=user)
            else:
                queryset = queryset.annotate(last_buying_date=Max('buying__date')).filter(
                    buying__date=F('last_buying_date'), buying__buyer=user)

        elif user:
            queryset = queryset.annotate(last_buying_date=Max('buying__date')).filter(
                buying__date=F('last_buying_date'), buying__buyer=user)

            # queryset = queryset.filter(user_id=user)
        return queryset


class PlotUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    lookup_url_kwarg = 'id_plot'
    queryset = Plot.objects.all()
    serializer_class = PlotUpdateSerializer

    def get_serializer_context(self):
        format = self.request.accepted_renderer.format if self.request.accepted_renderer else None
        fields = self.request.query_params.keys()
        context = {
            'request': self.request,
            'format': format,
        }

        if fields:
            context['fields'] = fields

        return context
