from rest_framework import serializers
from olympics.models import Athlete, Event

class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = [
            'pk',
            'name',
            'sex',
            'age',
            'height',
            'weight',
        ]
        read_only_fields = ['pk']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'pk',
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
        read_only_fields = ['pk']
