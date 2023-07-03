5
#CONF_START
EXPORT_PATH = None
PLANETS = {'Меркурий': 40, 'Венера': 45, 'Земля': 30, 'Марс': 32, 'Юпитер': 42, 'Сатурн': 45, 'Уран': 55, 'Нептун': 24, 'Плутон': 30, 'Эрида': 25, 'Хаумеа': 45, 'Макемаке': 55, 'Церера': 25, 'Луна': 30, 'Фобос': 45, 'Деймос': 24, 'Ио': 84, 'Европа': 45, 'Ганимед': 24, 'Каллисто': 45, 'Титан': 13, 'Энцелад': 45, 'Мимас': 32, 'Миранда': 25, 'Ариэль': 75, 'Умбриэль': 45, 'Тритон': 34, 'Харон': 23, 'Proxima b': 44, 'Proxima c': 23, 'TRAPPIST-1b': 24, 'TRAPPIST-1c': 44, 'TRAPPIST-1d': 56, 'TRAPPIST-1e': 24, 'TRAPPIST-1f': 55, 'TRAPPIST-1g': 52, 'TRAPPIST-1h': 45, 'Kepler-186b': 48, 'Kepler-186c': 44, 'Kepler-186d': 25, 'Kepler-186e': 44, 'Kepler-186f': 55, 'Луна TRAPPIST-1b': 24, 'Луна TRAPPIST-1c': 23, 'Луна TRAPPIST-1e': 24}
#CONF_END
import bpy

bpy.data.texts["nodes.py"].as_module()
app = bpy.data.texts["app.py"].as_module()

app.act(PLANETS, EXPORT_PATH)

