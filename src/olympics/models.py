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
