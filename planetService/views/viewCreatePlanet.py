from ..models import Planet, Plot
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from ..blenderApi.planetBuild import BlenderApi
from userService.models import User
from buyingService.models import Buying
import random
import string


class CreatePlanetPlot(APIView):
    permission_classes = [IsAdminUser]
    authentication_classes = []

    def get(self, response):
        Response({})


class CreatePlots(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]

    def get(self, response):
        planets = Planet.objects.all()
        instance = BlenderApi(planets)
        planets = instance.create_plots()
        users = User.objects.all()
        Buying.objects.all().delete()
        for planet in planets:
            for plot in planet["plots"]:
                probability = random.random()
                if probability > 0.3:
                    user = None
                else:
                    user = random.choice(users)
                price = random.randint(8500, 1000000)
                plot_obj, created = Plot.update_or_create_plot(
                    name=plot["plot_name"],
                    planet=Planet.objects.get(id=planet["planet_id"]),
                    mesh=plot["mesh"],
                    color='#' + ''.join(random.choices(string.hexdigits[:16], k=6)),
                    area=plot["area"],
                    owner=user,
                    price=plot["area"] * price * 8,
                    isSale=0 if user and random.random() > 0.2 else 1,
                    markUp=random.randint(0, 20) * (plot["area"] * price * 8) / 100 if user else 0,
                )
                if user:
                    Buying.objects.create(
                        plot=plot_obj,
                        cost=price,
                        buyer=user,
                        owner=None,
                    )
        return Response(planets)
