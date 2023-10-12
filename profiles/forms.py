from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    """Form to create a profile"""
    class Meta:
        model = Profile
        fields = ["image", "bio" , "age", "weight"]

        labels = {
            "image": "Avatar",
            "bio": "Bio",
            "age": "Age",
            "weight": "Weight"
        }