from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Tracker
from .forms import TrackerForm
from django.contrib.auth.mixins import LoginRequiredMixin

class Trackers(ListView):
    """ View all food """
    template_name = 'tracker/trackers.html'
    model = Tracker
    context_object_name = 'trackers'

    def get_queryset(self):
        return Tracker.objects.all().order_by('-date')   

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
