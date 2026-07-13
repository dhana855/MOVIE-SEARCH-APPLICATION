from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name="home"),

    path("movies/", views.movies, name="movies"),

    path("series/", views.series, name="series"),

    path("trending/", views.trending, name="trending"),

    path("toprated/", views.toprated, name="toprated"),

    path("watchlist/", views.watchlist, name="watchlist"),

    path("settings/", views.settings, name="settings"),

    path("details/<int:id>/", views.details, name="details"),
    
    path("api/movies/", views.movie_api, name="movie_api"),
    
    path("api/trending/", views.trending_api, name="trending_api"),
    
    path("api/recent/", views.recent_api, name="recent_api"),
    
    path("api/series/", views.series_api, name="series_api"),

]