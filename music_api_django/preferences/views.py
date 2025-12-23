from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Preference
from .serializers import PreferenceSerializer
from users.models import User


class PreferenceListCreateView(APIView):
    """
    POST /users/{user_id}/preferences/
    GET  /users/{user_id}/preferences/
    """

    def get(self, request, user_id):
        preferences = Preference.objects.filter(user_id=user_id)
        serializer = PreferenceSerializer(preferences, many=True)
        return Response(serializer.data)

    def post(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(
                {"detail": "Usuario no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )

        data = request.data.copy()
        data["user"] = user.id

        serializer = PreferenceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PreferenceDetailView(APIView):
    """
    DELETE /users/{user_id}/preferences/{pref_id}/
    """

    def delete(self, request, user_id, pref_id):
        try:
            preference = Preference.objects.get(pk=pref_id, user_id=user_id)
        except Preference.DoesNotExist:
            return Response(
                {"detail": "Preferencia no encontrada"},
                status=status.HTTP_404_NOT_FOUND
            )

        preference.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
