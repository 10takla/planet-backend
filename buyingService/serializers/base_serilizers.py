from rest_framework import serializers
from buyingService.models import Buying, Basket
from userService.serializer import UserSerializer


class BuyingSerializer(serializers.ModelSerializer):
    buyer = UserSerializer(context={'mode': 'conf_user'})
    owner = UserSerializer()
    cost = serializers.ReadOnlyField()

    class Meta:
        model = Buying
        fields = "__all__"


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = "__all__"
