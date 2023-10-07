from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Tracker


class TrackerForm(forms.ModelForm):
    """
    Form to create a Tacker
    """
    class Meta:
        model = Tracker
        fields = ['title', 'date', 'portion_size', 'meal_type', 'image', 'image_alt']

        description = forms.CharField(widget=RichTextWidget())

        labels = {
            'title': 'Name of food or meal',
            'date': 'Date when the food was consumed',
            'portion_size': 'Amount in gms',
            'meal_type': 'Type of the meal',
            'image': 'Image',
            'image_alt': 'Describe Image'      
        }