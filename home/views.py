from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView
from tracker.models import Tracker
from django.shortcuts import render
from datetime import datetime, timedelta


# Create your views here.


class Index(ListView):
    """A ListView for displaying the most recent Tracker entries"""
    template_name = "home/index.html"
    model = Tracker
    context_object_name = "trackers"

    def get_queryset(self):
        return self.model.objects.all()[:3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calories = []
        dates = []

        if self.request.user.is_authenticated:
            # Fetch data for the last 7 days
            profile = self.request.user.profile
            start_date = datetime.now() - timedelta(days=7)
            trackers = Tracker.objects.filter(
                user=profile, date__gte=start_date
            ).order_by("date")

            for tracker in trackers:
                calories.append(tracker.calories)
                dates.append(tracker.date.strftime("%Y-%m-%d"))

        context["calories"] = calories
        context["dates"] = dates
        return context
