from django.db import models
from users.models import User

class Preference(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="preferences"
    )

    genre = models.CharField(max_length=50, blank=True)
    favorite_artists = models.JSONField(blank=True, null=True)
    favorite_tracks = models.JSONField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Preferences of {self.user.username}"
