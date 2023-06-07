5
#CONF_START
EXPORT_PATH = 'C:/Users/letif/PycharmProjects/pythonProject/buyplanet/media/models/planets/'
PLANETS = {'Mercury': 40, 'Venus': 30, 'Earth': 55, 'Mars': 80, 'Jupiter': 120, 'Saturn': 400, 'Uranus': 260, 'Neptune': 20, 'Pluto': 20, 'Ceres': 20, 'Haumea': 20, 'Makemake': 20, 'Eris': 20}
#CONF_END
import bpy

bpy.data.texts["nodes.py"].as_module()
app = bpy.data.texts["app.py"].as_module()

app.act(PLANETS)

