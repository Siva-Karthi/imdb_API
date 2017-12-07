from django.contrib import admin
from .models import MovieModel,GenreModel

admin.site.register([MovieModel,GenreModel])
