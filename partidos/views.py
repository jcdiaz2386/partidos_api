from rest_framework import generics
from .models import PartidoPolitico
from .serializers import PartidoPoliticoSerializer

class PartidoPoliticoList(generics.ListCreateAPIView):
    queryset = PartidoPolitico.objects.all()
    serializer_class = PartidoPoliticoSerializer
