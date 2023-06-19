from rest_framework import serializers
from buyingService.models import Buying, Basket
from userService.serializer import UserSerializer
from planetService.serializers import PlotSerializer


class BuyingCreateSerializer(serializers.ModelSerializer):
    buyer = UserSerializer(read_only=True, context={'mode': 'conf_user'})
    owner = UserSerializer(read_only=True)
    cost = serializers.ReadOnlyField()
    plot = PlotSerializer(read_only=True, context={'fields': ['cost']})

    class Meta:
        model = Buying
        fields = "__all__"
        extra_kwargs = {'plot': {'required': True}}


class BasketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = "__all__"
