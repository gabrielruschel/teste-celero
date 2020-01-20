from django.urls import path
from .views import AthleteRudView,AthleteListCreateView,EventRudView,EventListCreateView

urlpatterns = [
    path('athlete/<int:pk>/', AthleteRudView.as_view(), name='athlete-rud'),
    path('athlete/', AthleteListCreateView.as_view(), name='athlete-list-create'),
    path('event/<int:pk>/', EventRudView.as_view(), name='event-rud'),
    path('event/', EventListCreateView.as_view(), name='event-list-create'),
]
