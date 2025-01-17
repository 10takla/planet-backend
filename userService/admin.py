from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'wallet', 'logo')
    list_editable = ('username', 'password', 'wallet', 'logo')


admin.site.register(User, UserAdmin)
