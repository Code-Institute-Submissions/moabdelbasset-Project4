from django.urls import path
from .views import AddTracker

urlpatterns = [
    path('', AddTracker.as_view(), name='add_tracker'),
]