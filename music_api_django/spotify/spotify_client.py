import os
import requests
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

TOKEN_URL = "https://accounts.spotify.com/api/token"
BASE_URL = "https://api.spotify.com/v1"


def get_access_token():
    """
    Obtiene el token de acceso usando Client Credentials
    """
    response = requests.post(
        TOKEN_URL,
        data={"grant_type": "client_credentials"},
        auth=(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET),
        timeout=10
    )
    response.raise_for_status()
    return response.json()["access_token"]


def spotify_search(query: str, type: str = "track", limit: int = 5):
    """
    Busca artistas o canciones en Spotify
    """
    token = get_access_token()
    headers = {
        "Authorization": f"Bearer {token}"
    }

    params = {
        "q": query,
        "type": type,
        "limit": limit
    }

    response = requests.get(
        f"{BASE_URL}/search",
        headers=headers,
        params=params,
        timeout=10
    )
    response.raise_for_status()
    return response.json()

def get_artist_top_tracks(artist_id: str, market: str = "US"):
    """
    Obtiene las canciones más populares de un artista
    """
    token = get_access_token()
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        f"{BASE_URL}/artists/{artist_id}/top-tracks",
        headers=headers,
        params={"market": market},
        timeout=10
    )
    response.raise_for_status()
    return response.json()
