from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView
from tracker.models import Tracker
from django.shortcuts import render


# Create your views here.

class Index(ListView):
    template_name = 'home/index.html'
    model = Tracker
    context_object_name = 'trackers'

    def get_queryset(self):
        return self.model.objects.all()[:3]
    