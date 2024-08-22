from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genres', 'show_actors', 'release_date', 'resume')
    search_fields = ('title',)
    list_filter = ('genres',)

    def show_actors(self, obj):
        return ", ".join([str(actor) for actor in obj.actors.all()])

    show_actors.short_description = "Atores"
