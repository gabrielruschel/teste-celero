from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse
from olympics.models import Athlete,Event

class AthleteTests(APITestCase):
    def test_create_athlete(self):
        """
        Basic test for Athlete create in the API
        """

        url = reverse('api-olympics:athlete-list-create')
        data = {'name':'test','sex':'M','age':'25','height':'160','weight':'70'}
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Athlete.objects.count(), 1)
        self.assertEqual(Athlete.objects.get().name, 'test')

    def test_list_athlete(self):
        """
        Basic test for Athlete list in the API
        """

        url = reverse('api-olympics:athlete-list-create')
        data = {}
        response = self.client.get(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class EventTests(APITestCase):
    def setUp(self):
        athlete_obj = Athlete(name='testeatl',sex='M',age='25',height='160',weight='70')
        athlete_obj.save()

    def test_single_athlete(self):
        """
        Basic test to check if there is one Athlete created from the setUp function
        """

        atl_count = Athlete.objects.count()
        self.assertEqual(atl_count,1)

    def test_create_event(self):
        """
        Basic test for Event create in the API
        """

        atl_id = Athlete.objects.first().id
        url = reverse('api-olympics:event-list-create')
        data = {'athlete':atl_id,'team':'Test','noc':'ABC','games':'teste','year':2000,'season':'teste','city':'teste','sport':'teste','event':'teste','medal':'teste'}
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(Event.objects.get().event, 'teste')

    def test_list_event(self):
        """
        Basic test for Event list in the API
        """

        url = reverse('api-olympics:event-list-create')
        data = {}
        response = self.client.get(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
