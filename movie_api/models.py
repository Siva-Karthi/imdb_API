# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# 
# from django.db import models
# 
# # Create your models here.
# 
# class Genre(models.Model):
#     genre = models.CharField(max_length=255)
# 
#     #def __unicode__(self):
#     #    return u'%s' % (self.genre)
#     def __str__(self):
#         return self.name
# 
# class Movie(models.Model):
#     name = models.CharField(max_length=100)
#     director = models.CharField(max_length=100)
#     popularity = models.DecimalField(max_digits=4, decimal_places=1)
#     imdb_score = models.DecimalField(max_digits=2, decimal_places=1)
#     genre = models.ManyToManyField(Genre)
# 
#     def __str__(self):
#         return self.name
from django.db import models

# Create your models here


class GenreModel(models.Model):
    genre_name = models.CharField(max_length=100,primary_key=True,unique=True)

    def __unicode__(self):
        return u'%s' % (self.genre_name)


class MovieModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    director = models.CharField(max_length=100)
    popularity_99 = models.DecimalField(max_digits=4, decimal_places=1)
    imdb_score = models.DecimalField(max_digits=4, decimal_places=1)
    genre = models.ManyToManyField(GenreModel)
    search_fields = ['name','director','popularity_99','imdb_score']

    def __unicode__(self):
        return u'%s' % (self.name)
