import os
from django.conf import settings


def directory_tree(path, dirs=[], result={}):
    for dir_name in os.listdir(path):
        pt = os.path.join(path, dir_name)
        if os.path.isdir(pt):
            result[dir_name] = {}
            directory_tree(pt, dirs + [dir_name], result[dir_name])
        if os.path.isfile(pt):
            for img_name in os.listdir(path):
                result[img_name.split('.')[0]] = os.path.join(
                    "textures", '/'.join(dirs), img_name)

    return result


def set_limit(request, queryset, parameters=None):
    if parameters is None:
        parameters = [["from", 0], ["to", 10]]

    limit_from = request.GET.get(parameters[0][0]) or parameters[0][1]
    limit_to = request.GET.get(parameters[1][0]) or parameters[1][1]

    return queryset[int(limit_from): int(limit_to)]
