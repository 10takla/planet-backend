from rest_framework import serializers
import os
from planetService.models import Planet, Plot
from django.conf import settings
from planetService.helpers import directory_tree
from buyingService.serializers import BuyingSerializer, BasketSerializer
from buyingService.models import Buying, Basket
from django.db.models import F, Max, Q
from userService.serializer import UserSerializer

class PlanetSerializer(serializers.ModelSerializer):
    textures = serializers.SerializerMethodField()
    plots = serializers.SerializerMethodField()

    class Meta:
        model = Planet
        fields = "__all__"

    def get_plots(self, obj):
        request = self.context['request']

        params = {}
        for key, value in request.query_params.items():
            if key.startswith('plots_'):
                params[key.replace('plots_', '')] = value

        queryset = obj.plot_set.all()

        if 'me' in request.path:
            queryset = queryset.filter(user=request.user)

        if params.get('search'):
            queryset = queryset.filter(name__icontains=params['search'])

        if params.get('from') or params.get('to'):
            limit_from, limit_to = params.get('from', 0), params.get('to', 10)
            queryset = queryset[int(limit_from): int(limit_to)]

        serializer = PlotSerializer(queryset, many=True,
                                    context={
                                        **self.context,
                                        'fields': params.get('fields', '').split(',')
                                    })

        return serializer.data

    def get_textures(self, obj):
        directory = os.path.join(settings.MEDIA_ROOT, 'textures', obj.name)

        if os.path.exists(directory) and os.path.isdir(directory):
            return directory_tree(directory, [obj.name], {})
        return []

    def __init__(self, *args, **kwargs):
        context = kwargs.get('context', {})

        fields = set(context.get('fields', ''))

        all_fields = set(self.fields.keys())
        base_fields = {'id', 'name'}

        fields = fields.union(base_fields).intersection(all_fields)

        super().__init__(*args, **kwargs)

        for field_name in all_fields - fields:
            self.fields.pop(field_name)


class PlotSerializer(serializers.ModelSerializer):
    planet = PlanetSerializer(context={"fields": ["textures", "color"]})
    storyBuying = serializers.SerializerMethodField()
    cost = serializers.SerializerMethodField()
    basket = serializers.SerializerMethodField()
    surfaceArea = serializers.SerializerMethodField()
    owner = UserSerializer()
    # owner = serializers.SerializerMethodField()
    #
    # def get_owner(self, obj):
    #     buying = obj.buying_set.select_related('buyer').order_by('-date').first()
    #     if buying:
    #         buying_serializer = BuyingSerializer(buying)
    #         return buying_serializer.data.get('buyer')
    #     return None

    def get_surfaceArea(slf, obj):
        return obj.planet.surface_area * obj.area

    def get_basket(self, obj):
        request = self.context.get('request')
        # print( self.context)
        if request:
            user = request.user
            plot = obj
            # print(user, plot)
            queryset = Basket.objects.filter(user=user, plot=plot).first()
            if queryset:
                serializer = BasketSerializer(queryset)
                return serializer.data
            else:
                return None
        else:
            return None

    class Meta:
        model = Plot
        fields = "__all__"

    def get_cost(self, obj):
        price = obj.price
        mark_up = obj.markUp
        cost = price + mark_up
        return cost

    def get_storyBuying(self, obj):
        buying_queryset = Buying.objects.filter(plot=obj).order_by('date')
        serializer = BuyingSerializer(buying_queryset, many=True)
        return serializer.data

    def __init__(self, *args, **kwargs):
        context = kwargs.get('context', {})
        fields = set(context.get('fields', ''))
        user_fields = {"storyBuying"}

        if not context.get("for_user", None):
            fields = fields.difference(user_fields)

        all_fields = set(self.fields.keys())
        base_fields = {'id', 'name'}

        fields = fields.union(base_fields).intersection(all_fields)
        super().__init__(*args, **kwargs)
        if fields is not None:
            for field_name in all_fields - fields:
                self.fields.pop(field_name)


class PlotUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plot
        fields = ["isSale", "price", "markUp"]

    def __init__(self, *args, **kwargs):
        context = kwargs.get('context', {})
        fields = set(context.get('fields', ''))

        all_fields = set(self.fields.keys())
        super().__init__(*args, **kwargs)
        if fields is not None:
            for field_name in all_fields - fields:
                self.fields.pop(field_name)
