from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Review
from .serializers import ReviewSerializer
from app.permissions import GlobalDefaultPermission


class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
