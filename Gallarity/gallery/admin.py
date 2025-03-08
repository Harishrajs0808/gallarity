from django.contrib import admin # type: ignore
from .models import User, Wallpaper

admin.site.register(User)
admin.site.register(Wallpaper)
