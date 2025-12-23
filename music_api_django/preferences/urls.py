from django.urls import path
from .views import PreferenceListCreateView, PreferenceDetailView

urlpatterns = [
    path("users/<int:user_id>/preferences/", PreferenceListCreateView.as_view()),
    path(
        "users/<int:user_id>/preferences/<int:pref_id>/",
        PreferenceDetailView.as_view()
    ),
]
