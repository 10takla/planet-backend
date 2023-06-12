from rest_framework import serializers
from planetService.models import Plot

class PlotFirstViewSerializer(serializers.ModelSerializer):
    cost = serializers.SerializerMethodField()

    class Meta:
        model = Plot
        fields = ['id', 'name', 'cost']

    def get_cost(self, obj):
        price = obj.price
        mark_up = obj.markUp
        cost = price + mark_up
        return cost