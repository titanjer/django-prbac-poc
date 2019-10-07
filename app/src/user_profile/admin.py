from django.contrib import admin

# Register your models here.

from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile

    list_display = [
        'user',
        'role_user',
        'role_admin',
    ]


admin.site.register(UserProfile, UserProfileAdmin)
