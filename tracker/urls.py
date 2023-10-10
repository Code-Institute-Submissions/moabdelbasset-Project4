from django.urls import path
from .views import AddTracker
from .views import Trackers, DeleteTracker

urlpatterns = [
    path('', AddTracker.as_view(), name='add_tracker'),
    path('trackers/', Trackers.as_view(), name='trackers'),
    path('delete/<slug:pk>/', DeleteTracker.as_view(), name="delete_tracker"),
]