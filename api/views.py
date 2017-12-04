# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from api.models import MovieModel
from api.serializers import MovieSerializer
from .permissions import IsAdminOrReadOnly

#from rest_framework.throttling import UserRateThrottle
from throttles import BurstRateThrottle,SustainedRateThrottle

class MovieCreateView(ListCreateAPIView):
    queryset = MovieModel.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAdminOrReadOnly, )

class MovieDetailView(RetrieveUpdateDestroyAPIView):

    #Throttle gettting movie detail 
    throttle_classes = (BurstRateThrottle,SustainedRateThrottle)
    #throttle_scope = "uploads"

    queryset = MovieModel.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAdminOrReadOnly, )

class SearchAPIView(APIView):
    """
        APIView for search.Only get method is defined.
    """
    def get(self, request, movie_name):
        """takes movie_name as get parameter"""
        if movie_name:
            movies = MovieModel.objects.filter(name__icontains=movie_name)
            movies_serializer = MovieSerializer(movies, many=True)
            return Response(movies_serializer.data)
