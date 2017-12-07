from django.conf.urls import url
from django.contrib import admin

from .views import (
	MovieListAPIView,
        MovieCreateAPIView,
	MovieDetailAPIView,
	MovieUpdateAPIView,
	MovieDeleteAPIView,
        login_view,
        logout_view
	)
# from django.contrib.auth import views as auth_views
# from django.views.generic.base import TemplateView

app_name = 'movie_api'
urlpatterns = [    
    url(r'^$', MovieListAPIView.as_view(), name='movies_list'),
    # url(r'^$',login_view,name = 'home' ),
    url(r'^login/',login_view,name = 'login' ),
    url(r'^logout/',logout_view,name = 'logout' ),
    url(r'^create/$', MovieCreateAPIView.as_view(), name='create'),
    url(r'^(?P<name>[\w-]+)/$', MovieDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<name>[\w-]+)/edit/$', MovieUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<name>[\w-]+)/delete/$', MovieDeleteAPIView.as_view(), name='delete')
]
