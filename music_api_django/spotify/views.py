import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from preferences.models import Preference
from .spotify_client import spotify_search, get_artist_top_tracks


log = logging.getLogger(__name__)

class SpotifySearchView(APIView):
    """
    GET /spotify/search?q=...&type=track|artist
    """

    def get(self, request):
        query = request.query_params.get("q")
        search_type = request.query_params.get("type", "track")

        if not query:
            return Response(
                {"detail": "El parámetro 'q' es obligatorio"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if search_type not in ["track", "artist"]:
            return Response(
                {"detail": "El parámetro 'type' debe ser 'track' o 'artist'"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            data = spotify_search(query=query, type=search_type)
            return Response(data)
        except Exception as e:
            return Response(
                {"detail": "Error al comunicarse con Spotify"},
                status=status.HTTP_502_BAD_GATEWAY
            )

class SpotifyUserFavoritesView(APIView):
    """
    GET /spotify/users/{id}/favorites
    """

    def get(self, request, user_id):
        # User
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(
                {"detail": "Usuario no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )

        # Preferences
        pref = Preference.objects.filter(user=user).first()
        if not pref:
            return Response(
                {"detail": "El usuario no tiene preferencias registradas"},
                status=status.HTTP_404_NOT_FOUND
            )

        # Artists
        if not pref.favorite_artists or len(pref.favorite_artists) == 0:
            return Response(
                {"detail": "No hay artistas favoritos para buscar"},
                status=status.HTTP_400_BAD_REQUEST
            )

        artist_query = pref.favorite_artists[0]

        try:
            artist_result = spotify_search(
                query=artist_query,
                type="artist",
                limit=1
            )
            artist_items = artist_result.get("artists", {}).get("items", [])

            if not artist_items:
                return Response(
                    {"detail": "Artista no encontrado en Spotify"},
                    status=status.HTTP_404_NOT_FOUND
                )

            artist_id = artist_items[0].get("id")
        except Exception:
            log.exception("Error buscando artista en Spotify")
            return Response(
                {"detail": "Error al buscar artista en Spotify"},
                status=status.HTTP_502_BAD_GATEWAY
            )

        # Top tracks
        try:
            top_tracks = get_artist_top_tracks(artist_id)
        except Exception:
            log.exception("Error obteniendo top tracks")
            return Response(
                {"detail": "Error al obtener top tracks del artista"},
                status=status.HTTP_502_BAD_GATEWAY
            )

        # Favorite tracks
        if not pref.favorite_tracks or len(pref.favorite_tracks) < 2:
            return Response(
                {"detail": "No hay suficientes canciones favoritas para buscar"},
                status=status.HTTP_400_BAD_REQUEST
            )

        track_query = pref.favorite_tracks[1]

        try:
            track_result = spotify_search(
                query=track_query,
                type="track",
                limit=1
            )
        except Exception:
            log.exception("Error buscando track")
            return Response(
                {"detail": "Error al buscar la canción en Spotify"},
                status=status.HTTP_502_BAD_GATEWAY
            )

        # Response
        return Response({
            "user": user.username,
            "artist_searched": artist_query,
            "artist_top_tracks": top_tracks,
            "track_searched": track_query,
            "track_info": track_result
        })