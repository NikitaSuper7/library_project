from django.contrib import admin
from users.models import CustomUser

# Register your models here.


@admin.register(CustomUser)
class AuthorAdmin(admin.ModelAdmin):
    exclude = ("password",)
