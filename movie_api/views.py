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
        search_fields = ['name','director']
        def get_queryset(self):
	    queryset = MovieModel.objects.all()
            movie_to_search = self.request.query_params.get('name')
            director_to_search = self.request.query_params.get('director')
            if movie_to_search:
               queryset = queryset.filter(name=movie_to_search)
            if director_to_search:
               queryset = queryset.filter(director=director_to_search)
                 
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
