from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse


class Profiles(TemplateView):
    """User Profile View"""

    template_name = "profiles/profile.html"

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(user=self.kwargs["pk"])
        context = {"profile": profile, "form": ProfileForm(instance=profile)}
        return context


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a profile"""

    form_class = ProfileForm
    model = Profile
    template_name = "profiles/profile.html"

    def form_valid(self, form):
        self.success_url = reverse("profile", args=[str(self.kwargs["pk"])])
        return super().form_valid(form)

    def get_object(self, queryset=None):
        user = User.objects.get(pk=self.kwargs["pk"])
        return user.profile

    def test_func(self):
        return self.request.user == self.get_object().user
