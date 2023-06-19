5
#CONF_START
EXPORT_PATH = None
PLANETS = {'Плутон': 30, 'Эрида': 25, 'Венера': 45, 'Марс': 32, 'Нептун': 24, 'Меркурий': 40, 'Земля': 30, 'Юпитер': 42, 'Сатурн': 45, 'Уран': 55}
#CONF_END
import bpy

bpy.data.texts["nodes.py"].as_module()
app = bpy.data.texts["app.py"].as_module()

app.act(PLANETS, EXPORT_PATH)

