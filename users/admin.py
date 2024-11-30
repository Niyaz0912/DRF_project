from django.contrib import admin
from users.models import User


@admin.register(User)
class CourseAdmin(admin.ModelAdmin):
    """Модель User зарегистрирована в админке"""
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_active',)
    list_filter = ('id', 'email',)
    ordering = ('id',)
