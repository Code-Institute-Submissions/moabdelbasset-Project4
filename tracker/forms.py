from django import forms
from djrichtextfield.widgets import RichTextWidget
from django.forms.widgets import DateInput
from datetime import date
from .models import Tracker


class TrackerForm(forms.ModelForm):
    """
    Form to create a Tacker
    """
    class Meta:
        model = Tracker
        fields = ['title', 'date', 'portion_size', 'meal_type', 'image', 'image_alt']

        description = forms.CharField(widget=RichTextWidget())

        widgets = {
            'date': DateInput(attrs={'type': 'date', 'max': date.today().strftime('%Y-%m-%d')}),
        }

        labels = {
            'title': 'Name of food or meal',
            'date': 'Date when the food was consumed',
            'portion_size': 'Amount in gms',
            'meal_type': 'Type of the meal',
            'image': 'Image',
            'image_alt': 'Describe Image'      
        }

        def clean_date(self):
            selected_date = self.cleaned_data.get('date')
            if selected_date and selected_date > date.today():
                raise forms.ValidationError("The date cannot be in the future.")
            return selected_date