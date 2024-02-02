from django.contrib import admin
from .models import Fungi, Habitat


class ShowFungiAdmin(admin.ModelAdmin):
    list_display = ("CommonName", "LatinName","id")
    search_fields = ['CommonName','LatinName','id']


admin.site.register(Fungi,ShowFungiAdmin)
admin.site.register(Habitat)


