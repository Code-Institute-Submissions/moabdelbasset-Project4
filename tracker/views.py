from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Tracker
from .forms import TrackerForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class AddTracker(LoginRequiredMixin, CreateView):
    """
    Add a tracker view
    """
    template_name = 'tracker/add_tracker.html'
    model = Tracker
    form_class = TrackerForm
    success_url = '/tracker/'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super(AddTracker, self).form_valid(form)
