from django.contrib import admin
from .models import Fungi


class ShowFungiAdmin(admin.ModelAdmin):
    list_display = ("CommonName", "LatinName","id")


admin.site.register(Fungi,ShowFungiAdmin)


