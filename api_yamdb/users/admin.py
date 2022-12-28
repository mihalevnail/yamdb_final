from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'username', 'first_name', 'last_name', 'role', 'email'
    )
    list_editable = ('role',)
    search_fields = ('username',)
    list_filter = ('username', 'email')
    empty_value_display = '--пусто--'
