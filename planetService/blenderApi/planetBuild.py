import os
import subprocess
import psutil
from django.conf import settings


class BlenderApi:
    name_blend = "sadasdasdled.blend"

    blender_path = "D:/Program Files/blender-3.6.0-alpha+main.e4eb9e04e016-windows.amd64-release/blender.exe"
    blend_file_path = "C:/Users/letif\OneDrive/Рабочий стол/" + name_blend
    script_name = os.path.join(settings.BASE_DIR, 'planetService/blenderApi/script_text.py')
    configs = {
        # "EXPORT_PATH": "C:/Users/letif/PycharmProjects/pythonProject7/planets/media/models/planets/",
        "EXPORT_PATH": None
    }

    def __init__(self, planets: list, export_path: str = None):
        self.planets = planets
        self.export_path = export_path

    def create_plots(self):
        self.change_config(self.planets, self.export_path)
        self.change_script(self.configs)
        parse = self.run_script()
        return self.parse(parse)

    def change_config(self, planets, export_path=None):
        if planets and len(planets):
            planets_conf = {}
            for planet in planets:
                if planet.plots_count >= 6:
                    planets_conf[planet.name] = planet.plots_count

            self.configs["PLANETS"] = planets_conf
        if export_path:
            self.configs["EXPORT_PATH"] = export_path

    def change_script(self, configs):
        # преобразовать конфиг под блендер конфиг
        str_conf = ''
        for key, value in configs.items():
            str_conf += f"{key} = {repr(value)}\n"

        # вставить конфиг в скрипт
        with open(self.script_name, 'r', encoding="utf-8") as file:
            parse = file.read()
            start, end = '#CONF_START\n', '#CONF_END\n'
            str_conf = start + str_conf + end
            text = parse.split(start)[0] + str_conf + parse.split(end)[1]
            with open(self.script_name, 'w', encoding="utf-8") as file:
                file.write(text)

    def run_script(self):
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == 'blender.exe':
                proc.terminate()

        blender_process = subprocess.Popen(
            [self.blender_path, '-b', self.blend_file_path, "--python", self.script_name],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        blender_output, blender_error = blender_process.communicate()

        return blender_output.decode()

    # спарсить текст консоли блендера
    def parse(self, parse: str):
        return_planets = []
        planets = parse.split('START')[1].split("END")[0].split("NEXT")
        if planets != ['']:
            for id_planet, planet in enumerate(planets):
                planet_name, vertices, faces, centers, area = planet.split('|')
                vertices, faces, centers, area = [eval(i) for i in [vertices, faces, centers, area]]

                return_plots = []
                for i, face in enumerate(faces):
                    return_plot = {
                        "plot_name": '_Plot_'.join([planet_name, str(i)]),
                        "mesh": {"vertices": vertices[i], "faces": face, "center": centers[i]},
                        "area": area[i],
                    }
                    return_plots.append(return_plot)

                return_planet = {"planet_id": self.planets[id_planet].id, "plots": return_plots}
                return_planets.append(return_planet)

        return return_planets
