import csv

import os,django
from sys import argv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "teste.settings")
django.setup()

from olympics.models import Athlete

def populate_athletes():

    last_id = 0
    obj_list = []

    print("")
    print("-- Populando modelo de atletas --")
    print("")

    with open('athlete_events.csv') as rows:

        for row in csv.DictReader(rows, delimiter=","):
            if (int(row['ID']) == last_id):
                continue

            last_id = int(row['ID'])
            atl = Athlete(athlete_id=int(row['ID']),name=row['Name'],sex=row['Sex'],age=row['Age'],height=row['Height'],weight=row['Weight'])
            obj_list.append(atl)

    try:
        Athlete.objects.bulk_create(obj_list)
    except Exception as e:
        print(e)

def main():
    if (argv[1] == 'athlete'):
        populate_athletes()

if __name__ == "__main__":
    main()
