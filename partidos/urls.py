from django.urls import path
from .views import PartidoPoliticoList

urlpatterns = [
    path('api/partidos/', PartidoPoliticoList.as_view(), name='partido-politico-list'),
]
