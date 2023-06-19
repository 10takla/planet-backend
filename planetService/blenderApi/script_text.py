5
#CONF_START
EXPORT_PATH = None
PLANETS = {'Меркурий': 40, 'Венера': 50, 'Земля': 30, 'Марс': 55, 'Юпитер': 42, 'Сатурн': 45, 'Уран': 55}
#CONF_END
import bpy

bpy.data.texts["nodes.py"].as_module()
app = bpy.data.texts["app.py"].as_module()

app.act(PLANETS, EXPORT_PATH)

