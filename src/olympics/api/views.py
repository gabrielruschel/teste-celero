from rest_framework import generics
from olympics.models import Athlete,Event
from .serializers import AthleteSerializer,EventSerializer

class AthleteListCreateView(generics.ListCreateAPIView):
    """
    View for the Athlete endpoint that provides the List and Create functions for the Athlete model
    """

    lookup_field = 'pk'
    serializer_class = AthleteSerializer

    def get_queryset(self):
        queryset = Athlete.objects.all()

        #Filter by name
        query_param = self.request.query_params.get('name', None)
        if (query_param is not None):
            queryset = queryset.filter(name__icontains=query_param)

        #Filter by sex
        query_param = self.request.query_params.get('sex', None)
        if (query_param is not None):
            queryset = queryset.filter(sex__exact=query_param)

        #Filter by age
        query_param = self.request.query_params.get('age', None)
        if (query_param is not None):
            queryset = queryset.filter(age__exact=query_param)
        return queryset

    def perform_create(self,serializer):
        serializer.save()


class AthleteRudView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for the Athlete endpoint that provide the Retrieve, Update and Destroy functions for the Athlete model
    """

    lookup_field = 'pk'
    serializer_class = AthleteSerializer
    # queryset = Athlete.objects.all()

    def get_queryset(self):
        return Athlete.objects.all()

class EventRudView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for the Event endpoint that provides the Retrieve, Update and Destroy functions for the Event model
    """

    lookup_field = 'pk'
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()

class EventListCreateView(generics.ListCreateAPIView):
    """
    View for the Event endpoint that provides the List and Create functions for the Event model
    """

    lookup_field = 'pk'
    serializer_class = EventSerializer
    # queryset = Athlete.objects.all()

    def get_queryset(self):

        queryset =Event.objects.all()

        #Filter by team
        query_param = self.request.query_params.get('team', None)
        if (query_param is not None):
            queryset = queryset.filter(team__exact=query_param)

        #Filter by year
        query_param = self.request.query_params.get('year', None)
        if (query_param is not None):
            queryset = queryset.filter(year__exact=query_param)

        #Filter by season
        query_param = self.request.query_params.get('season', None)
        if (query_param is not None):
            queryset = queryset.filter(season__exact=query_param)

        #Filter by sport
        query_param = self.request.query_params.get('sport', None)
        if (query_param is not None):
            queryset = queryset.filter(sport__icontains=query_param)

        #Filter by medal
        query_param = self.request.query_params.get('medal', None)
        if (query_param is not None):
            queryset = queryset.filter(medal__exact=query_param)

        return queryset

    def perform_create(self,serializer):
        serializer.save()
