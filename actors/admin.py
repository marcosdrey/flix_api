from django.contrib import admin
from .models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    model = Actor
    list_display = ('id', 'name', 'birthday', 'nationality')
