from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('userService.urls'), name="userService"),
    path('planets/', include('planetService.urls'), name="planetService"),
    path('media/<path:path>', views.get_images),
]
