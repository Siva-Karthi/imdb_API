from rest_framework.generics import (ListAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	RetrieveDestroyAPIView,
        CreateAPIView,
	UpdateAPIView
	)
from models import (
	MovieModel	
	)
from serializers import MovieSerializer,MovieCreateSerializer,MovieListSerializer
from django.contrib.auth import (
                                 authenticate,
                                 get_user_model,
                                 login,
                                 logout                                 
                                 )
from django.shortcuts import redirect

from .forms import UserLoginForm
from django.shortcuts import render
from rest_framework.permissions import (
     AllowAny,
     IsAuthenticated,
     IsAdminUser,
     IsAuthenticatedOrReadOnly,
)

from rest_framework.filters import (
     SearchFilter,
     OrderingFilter,
     )

from paginations import ListMoviesPagination


def login_view(request):
    title = "login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
            print "hereee"
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password) 
            login(request, user)
            return  redirect ('movie_api:movies_list')
    # return  redirect ('movie_api:movies_list')
    return render(request, "forms.html",{"form":form,"title":title})   

def logout_view(request):
    logout(request)
    title = "login"
    form = UserLoginForm(request.POST or None)
    return render(request, "forms.html",{"form":form,"title":title})   

class MovieListAPIView(ListAPIView):
	"""
	List all available movies
	"""
	queryset = MovieModel.objects.all()
	serializer_class = MovieListSerializer
        permission_classes = [IsAuthenticated]
        filter_backends = [SearchFilter]
        pagination_class = ListMoviesPagination
        search_fields = ['name','director','popularity_99','imdb_score']
        def get_queryset(self):
	    queryset = MovieModel.objects.all()
            movie_to_search = self.request.query_params.get('name')
            director_to_search = self.request.query_params.get('director')
            genre_to_search = self.request.query_params.get('genre')
            popularity = self.request.query_params.get('popularity')
            popularity_gt = self.request.query_params.get('popularity_gt')
            popularity_lt = self.request.query_params.get('popularity_lt')
            imdb_score_to_search = self.request.query_params.get('imdb_score')
            imdb_score_gt = self.request.query_params.get('imdb_score_gt')
            imdb_score_lt = self.request.query_params.get('imdb_score_lt')

            if movie_to_search:
               # queryset = queryset.filter(name=movie_to_search)
               queryset = queryset.filter(name__iexact=movie_to_search)
            if director_to_search:
               queryset = queryset.filter(director__iexact=director_to_search)
            if genre_to_search:
	       queryset = queryset.filter(genre__genre_name__iexact=genre_to_search)
            if  popularity:
               queryset = queryset.filter(popularity_99=popularity)
            if  popularity_gt:
               queryset = queryset.filter(popularity_99__gt=popularity_gt)
            if  popularity_lt:
               queryset = queryset.filter(popularity_99__lt=popularity_lt)
            if  imdb_score_to_search:
               queryset = queryset.filter(imdb_score=imdb_score_to_search)
            if  imdb_score_gt:
               queryset = queryset.filter(imdb_score__gt=imdb_score_gt)
            if  imdb_score_lt:
               queryset = queryset.filter(imdb_score__lt=imdb_score_lt)
            return queryset

class MovieCreateAPIView(CreateAPIView):
	"""
	Create a movie
	"""
	queryset = MovieModel.objects.all()
	serializer_class = MovieCreateSerializer	
        permission_classes = [IsAuthenticated,IsAdminUser]

#class MovieUpdateAPIView(UpdateAPIView):
class MovieUpdateAPIView(RetrieveUpdateAPIView,):
	"""
	Update a movie details
	"""
	queryset = MovieModel.objects.all()
	serializer_class = MovieSerializer	
	lookup_field = 'name'
        permission_classes = [IsAuthenticated,IsAdminUser]

#class MovieDeleteAPIView(DestroyAPIView):
class MovieDeleteAPIView(RetrieveDestroyAPIView):
	"""
	Delete a movie from database
	"""
	queryset = MovieModel.objects.all()
	serializer_class = MovieSerializer
	lookup_field = 'name'	
        permission_classes = [IsAuthenticated,IsAdminUser]

class MovieDetailAPIView(RetrieveAPIView):
	"""
	Detail of a particular movie
	"""
	queryset = MovieModel.objects.all()
	serializer_class = MovieSerializer
	lookup_field = 'name'
        permission_classes = [IsAuthenticated]
	# lookup_url_kwarg = 'abc'
