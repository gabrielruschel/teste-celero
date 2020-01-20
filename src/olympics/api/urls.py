from django.urls import path
from .views import AthleteRudView

urlpatterns = [
    path('athlete/<int:pk>/', AthleteRudView.as_view(), name='athlete-rud'),
]
