from django.urls import path
from .views import AthleteRudView,AthleteCreateView

urlpatterns = [
    path('athlete/<int:pk>/', AthleteRudView.as_view(), name='athlete-rud'),
    path('athlete/', AthleteCreateView.as_view(), name='athlete-create'),
]
