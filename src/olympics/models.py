from django.db import models

# Create your models here.
class Athlete(models.Model):
    athlete_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    sex = models.CharField(max_length=1)
    age = models.CharField(max_length=4)
    height = models.CharField(max_length=4)
    weight = models.CharField(max_length=4)

    def __str__(self):
        return str(self.name)

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    team = models.CharField(max_length=35)
    noc = models.CharField(max_length=4)
    games = models.CharField(max_length=25)
    year = models.IntegerField()
    season = models.CharField(max_length=25)
    city = models.CharField(max_length=20)
    sport = models.CharField(max_length=35)
    event = models.CharField(max_length=80)
    medal = models.CharField(max_length=10)
