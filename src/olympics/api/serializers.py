from rest_framework import serializers
from olympics.models import Athlete, Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'athlete',
            'team',
            'noc',
            'games',
            'year',
            'season',
            'city',
            'sport',
            'event',
            'medal',
        ]
        read_only_fields = ['id']


class AthleteSerializer(serializers.ModelSerializer):
    athlete_event = EventSerializer(source="event_athlete",many=True,read_only=True)
    class Meta:
        model = Athlete
        fields = [
            'id',
            'name',
            'sex',
            'age',
            'height',
            'weight',
            'athlete_event',
        ]
        read_only_fields = ['id',]
