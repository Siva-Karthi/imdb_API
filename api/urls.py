from django.conf.urls import url

from api.views import MovieCreateView, MovieDetailView, SearchAPIView

urlpatterns = [
    # url(r'^movies/$', MovieCreateView.as_view(), name='movies'),
    #url(r'^movies/(?P<id>[0-9]+)$', MovieDetailView.as_view(), name='detail'),
    # url(r'^movies/(?P<pk>[0-9]+)$', MovieDetailView.as_view(), name='detail'),
    url(r'^movies[/]*$', MovieCreateView.as_view(), name='movies'),
    # url(r'^movies/(?P<pk>[0-9]+)[/]*$', MovieDetailView.as_view(), name='detail'),
    url('^search/(?P<movie_name>\w+)/$', SearchAPIView.as_view())
]
