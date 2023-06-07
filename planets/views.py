from django.http import JsonResponse
import os
from django.conf.urls.static import serve
from django.conf import settings


def get_images(request, path):
    full_path = os.path.join(settings.MEDIA_ROOT, path)

    if (os.path.isdir(full_path)):
        files = os.listdir(full_path)
        files = [os.path.join(settings.MEDIA_URL, path, name) for name in files]
        return JsonResponse({"images": files})
    elif os.path.isfile(full_path):
        try:
            return serve(request, os.path.basename(full_path), os.path.dirname(full_path))
        except :
            return JsonResponse({"error": "Файл не найден"}, status=404)
    else:
        return JsonResponse({"error": "Неверный путь"}, status=404)
