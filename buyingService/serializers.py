from rest_framework import serializers
from .models import Buying, Basket
from userService.serializer import UserSerializer
from planetService.serializers.firstViews_serializers import PlotFirstViewSerializer

class BuyingSerializer(serializers.ModelSerializer):
    buyer = UserSerializer(read_only=True, context={'mode': 'conf_user'})
    owner = UserSerializer(read_only=True)
    cost = serializers.ReadOnlyField()
    plot = PlotFirstViewSerializer(read_only=True)

    class Meta:
        model = Buying
        fields = "__all__"
        extra_kwargs = {'plot': {'required': True}}


class BuyingCreateSerializer(serializers.ModelSerializer):
    plot = serializers.IntegerField(required=False)
    cost = serializers.ReadOnlyField()
    buyer = serializers.ReadOnlyField()

    class Meta:
        model = Buying
        fields = "__all__"





class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = "__all__"
