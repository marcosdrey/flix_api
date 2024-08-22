from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Genre
from .serializers import GenreSerializer
from app.permissions import GlobalDefaultPermission


class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
