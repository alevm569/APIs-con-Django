from rest_framework import serializers
from .models import Preference


class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preference
        fields = [
            "id",
            "user",
            "genre",
            "favorite_artists",
            "favorite_tracks",
            "created_at",
        ]

    def validate_favorite_artists(self, value):
        if value is not None and not isinstance(value, list):
            raise serializers.ValidationError("favorite_artists debe ser una lista.")
        return value

    def validate_favorite_tracks(self, value):
        if value is not None and not isinstance(value, list):
            raise serializers.ValidationError("favorite_tracks debe ser una lista.")
        return value
