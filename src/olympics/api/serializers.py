from rest_framework import serializers
from olympics.models import Athlete

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
