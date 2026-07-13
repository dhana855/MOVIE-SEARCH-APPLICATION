from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "genre",
        "year",
        "rating",
        "featured",
        "trending",
        "recent",
    )

    search_fields = (
        "title",
        "genre",
    )

    list_filter = (
        "category",
        "genre",
        "year",
        "featured",
        "trending",
        "recent",
    )

    list_editable = (
        "featured",
        "trending",
        "recent",
    )

    ordering = (
        "-year",
        "-rating",
    )