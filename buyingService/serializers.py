from rest_framework import serializers
from .models import Buying, Basket
from userService.serializer import UserSerializer
from userService.models import User
from planetService.models import Plot
from django.shortcuts import get_object_or_404

class BuyingSerializer(serializers.ModelSerializer):
    buyer = UserSerializer(read_only=True)
    owner = UserSerializer(read_only=True)
    cost = serializers.ReadOnlyField()
    plot = serializers.PrimaryKeyRelatedField(queryset=Plot.objects.all())

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
