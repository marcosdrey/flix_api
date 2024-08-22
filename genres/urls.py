from django.urls import path
from .views import GenreListCreateView, GenreRetrieveUpdateDestroyView

urlpatterns = [
    path('', GenreListCreateView.as_view(), name='genre-list-create'),
    path('<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-rud')
]
