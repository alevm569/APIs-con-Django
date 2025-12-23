from django.urls import path
from .views import SpotifySearchView, SpotifyUserFavoritesView

urlpatterns = [
    path("spotify/search/", SpotifySearchView.as_view()),
    path(
        "spotify/users/<int:user_id>/favorites/",
        SpotifyUserFavoritesView.as_view()
    ),
]
