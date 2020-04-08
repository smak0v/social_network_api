from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
        'is_superuser',
        'last_login',
        'last_request',
    ]
    ordering = [
        'username',
        'email',
        'first_name',
        'last_name',
        'last_login',
        'last_request',
    ]
    search_fields = [
        'username',
        'email',
        'first_name',
        'last_name',
    ]
    list_filter = [
        'is_active',
        'is_staff',
        'is_superuser',
        'last_login',
        'last_request',
    ]
    list_per_page = 50


admin.site.register(User, UserAdmin)
