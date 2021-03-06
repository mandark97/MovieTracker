from django.conf.urls import url

import views.actors as actors
import views.movies as movies
from views.actions import search
import views.test as test
import views.signup as signup
from django.contrib.auth import views as auth_views
import views.watchlist as watchlist

urlpatterns = [
    url(r'^movies/$', movies.Index.as_view(), name='movies_index'),
    url(r'^movies/(?P<pk>[0-9]+)/$', movies.MovieDetailView.as_view(), name='movies_show'),
    url(r'^movies/(?P<pk_movie>[0-9]+)/actors/$', actors.Index.as_view(), name='movie_actors'),
    url(r'^actors/$', actors.Index.as_view(), name='actors_index'),
    url(r'^actors/(?P<pk>[0-9]+)/$', actors.Show.as_view(), name='actors_show'),
    url(r'^watched/$', actors.Index.as_view(),name='movies_watched'),
    url(r'^search/$', search, name='search'),
    url(r'^signup/$', signup.SignUp.as_view(), name='signup'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'movies_index'}, name='logout'),
    url(r'^watchlist/$', watchlist.Watchlist.as_view(), name='watchlist'),
]

