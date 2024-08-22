from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    title = models.CharField(max_length=500, verbose_name="Título")
    genres = models.ForeignKey(Genre, on_delete=models.PROTECT,
                               related_name='movies', verbose_name="Gêneros")
    release_date = models.DateField(null=True, blank=True, verbose_name="Data de Lançamento")
    actors = models.ManyToManyField(Actor, related_name='movies', verbose_name="Atores")
    resume = models.TextField(null=True, blank=True, verbose_name="Resumo")

    class Meta:
        ordering = ['title']
        verbose_name = 'Filme'

    def __str__(self):
        return self.title
