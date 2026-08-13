from django.shortcuts import render, get_object_or_404
from .models import Movie
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializer


def home(request):
    search = request.GET.get("search")

    movies = Movie.objects.all()

    if search:
        movies = movies.filter(title__icontains=search)

    context = {
        "movies": movies,
        "search": search,

        "featured_movies": Movie.objects.filter(featured=True)[:1],

        "trending_movies": Movie.objects.filter(trending=True),

        "recent_movies": Movie.objects.filter(recent=True).order_by("-id"),

        "continue_movies": Movie.objects.filter(continue_watch=True),

        "top_movies": Movie.objects.order_by("-rating")[:5],
    }

    return render(request, "home.html", context)


def movies(request):
    return render(request, "movie_list.html", {
        "movies": Movie.objects.filter(category="Movie"),
        "title": "🎬 Movies"
    })

def series(request):
    return render(request, "movie_list.html", {
        "movies": Movie.objects.filter(category="Series"),
        "title": "📺 Series"
    })


def trending(request):
    return render(request, "movie_list.html", {
        "movies": Movie.objects.filter(trending=True),
        "title": "🔥 Trending Movies"
    })


def toprated(request):
    return render(request, "movie_list.html", {
        "movies": Movie.objects.order_by("-rating"),
        "title": "⭐ Top Rated Movies"
    })

def watchlist(request):
    return render(request, "movie_list.html", {
        "movies": Movie.objects.filter(continue_watch=True),
        "title": "❤️ Watchlist"
    })


def settings(request):
    return render(request, "settings.html")


from django.shortcuts import render, get_object_or_404
from .models import Movie

def details(request, id):

    movie = get_object_or_404(Movie, id=id)

    similar_movies = Movie.objects.filter(
        genre=movie.genre
    ).exclude(id=movie.id)[:6]

    context = {
        "movie": movie,
        "similar_movies": similar_movies,
    }

    return render(request, "details.html", context)
    
    
    
    
    
@api_view(["GET"])
def movie_api(request):

    movies = Movie.objects.all()

    serializer = MovieSerializer(movies, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def trending_api(request):

    movies = Movie.objects.filter(trending=True)

    serializer = MovieSerializer(movies, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def recent_api(request):

    movies = Movie.objects.filter(recent=True)

    serializer = MovieSerializer(movies, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def series_api(request):

    movies = Movie.objects.filter(category="Series")

    serializer = MovieSerializer(movies, many=True)

    return Response(serializer.data)