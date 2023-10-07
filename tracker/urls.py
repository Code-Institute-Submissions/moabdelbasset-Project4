from django.urls import path
from .views import AddTracker
from .views import Trackers

urlpatterns = [
    path('', AddTracker.as_view(), name='add_tracker'),
    path('trackers/', Trackers.as_view(), name='trackers'),
]