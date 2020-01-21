import csv

import os,django
from sys import argv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "teste.settings")
django.setup()

from olympics.models import Athlete, Event

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
            atl = Athlete(id=int(row['ID']),name=row['Name'],sex=row['Sex'],age=row['Age'],height=row['Height'],weight=row['Weight'])
            obj_list.append(atl)

    try:
        Athlete.objects.bulk_create(obj_list)
    except Exception as e:
        print(e)

def populate_events():
    obj_list = []

    print("")
    print("-- Populando modelo de eventos --")
    print("")

    with open('athlete_events.csv') as rows:

        for row in csv.DictReader(rows, delimiter=","):

            atl_id = int(row['ID'])
            ev = Event(athlete_id=atl_id, team=row['Team'],noc=row['NOC'],games=row['Games'],year=row['Year'],season=row['Season'],city=row['City'],sport=row['Sport'],event=row['Event'],medal=row['Medal'])
            obj_list.append(ev)

    try:
        Event.objects.bulk_create(obj_list)
    except Exception as e:
        print(e)

def main():
    if (argv[1] == 'athlete'):
        populate_athletes()
    elif (argv[1] == 'event'):
        populate_events()

if __name__ == "__main__":
    main()
