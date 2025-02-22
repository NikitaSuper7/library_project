from django.contrib import admin
from .models import Author, Book, Review

# Register your models here.
# 1-ый вариант регистрации (более простой)
# admin.site.register(Author)


# 2-й вариант регистрации:
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "birth_date")
    list_filter = ("birth_date",)
    search_fields = (
        "first_name",
        "last_name",
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "publication_date",
        "author",
    )
    list_filter = (
        "publication_date",
        "author",
    )
    search_fields = (
        "title",
        "author__first_name",
        "author__last_name",
    )  # через __ обращаемся(переменной) к атрибуту другой модели


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "book",
        "rating",
    )
