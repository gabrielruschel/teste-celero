from django.urls import path
from .views import AthleteRudView,AthleteCreateView,EventRudView

urlpatterns = [
    path('athlete/<int:pk>/', AthleteRudView.as_view(), name='athlete-rud'),
    path('athlete/', AthleteCreateView.as_view(), name='athlete-create'),
    path('event/<int:pk>/', EventRudView.as_view(), name='event-rud')
]
