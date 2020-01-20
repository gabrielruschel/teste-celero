from rest_framework import generics
from olympics.models import Athlete
from .serializers import AthleteSerializer

class AthleteRudView(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = 'pk'
    serializer_class = AthleteSerializer
    # queryset = Athlete.objects.all()

    def get_queryset(self):
        return Athlete.objects.all()
