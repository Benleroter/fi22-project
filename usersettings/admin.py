from django.contrib import admin
from .models import Show, ShowSearchFields#, UserModes#, ShowGroup


class ShowAdmin(admin.ModelAdmin):
    #list_display = ("id", "user","ShowFungiNotes","slug")
    list_display = ("user", "ShowFungiNotes", "slug")
    #prepopulated_fields = {"slug": ("id",)}  # new
    # 'https://actorsfit.com/a?ID=00001-8b31500b-a5be-449c-aa7b-0d256758ce83'

class ShowSearchFieldsAdmin(admin.ModelAdmin):
    #list_display = ("id", "user","id","slug")
    list_display = ( "id","slug","user_id","user")
    #fields = ['id','user','slug']
    #prepopulated_fields = {"slug": ("id",)}  # new
    #'https://actorsfit.com/a?ID=00001-8b31500b-a5be-449c-aa7b-0d256758ce83'

admin.site.register(Show, ShowAdmin)
admin.site.register(ShowSearchFields, ShowSearchFieldsAdmin)

