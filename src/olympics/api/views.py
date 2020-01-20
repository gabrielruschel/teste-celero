from rest_framework import generics
from olympics.models import Athlete,Event
from .serializers import AthleteSerializer,EventSerializer

class AthleteListCreateView(generics.ListCreateAPIView):

    lookup_field = 'pk'
    serializer_class = AthleteSerializer
    # queryset = Athlete.objects.all()

    def get_queryset(self):
        return Athlete.objects.all()

    def perform_create(self,serializer):
        serializer.save()


class AthleteRudView(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = 'pk'
    serializer_class = AthleteSerializer
    # queryset = Athlete.objects.all()

    def get_queryset(self):
        return Athlete.objects.all()

class EventRudView(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = 'pk'
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()

class EventListCreateView(generics.ListCreateAPIView):

    lookup_field = 'pk'
    serializer_class = EventSerializer
    # queryset = Athlete.objects.all()

    def get_queryset(self):
        return Event.objects.all()

    def perform_create(self,serializer):
        serializer.save()
