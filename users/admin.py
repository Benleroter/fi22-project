from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('id','username', 'email', 'first_name', 'last_name','email', 'is_staff','is_active','date_joined', 'last_login') # Added last_login

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)