from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Actor
from .serializers import ActorSerializer
from app.permissions import GlobalDefaultPermission


class ActorListCreateView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
