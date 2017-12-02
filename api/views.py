# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.models import Movie
from api.serializers import MovieSerializer
from .permissions import IsAdminOrReadOnly


class MovieCreateView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAdminOrReadOnly, )

class MovieDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAdminOrReadOnly, )
