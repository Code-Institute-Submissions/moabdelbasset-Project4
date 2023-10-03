from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

# Create your models here.


class Tracker(models.Model):
    """"
    A model for calories tracker
    """
    MEAL_CHOICES = (
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snack', 'Snack'),
    )
    
    user = models.ForeignKey(User, related_name='tracker_entries', on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=False, blank=False)  # Name of the food or meal
    description = RichTextField(blank=True, null=True)  # Detailed description or notes
    date = models.DateField(null=False, blank=False)  # Date when the food was consumed
    calories = models.PositiveIntegerField(null=False, blank=False)  # Amount of calories
    portion_size = models.CharField(max_length=200, blank=True, null=True)  # Size or weight of the portion consumed
    meal_type = models.CharField(choices=MEAL_CHOICES, max_length=10, default='Snack')  # Type of meal
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the entry was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the entry was last updated
    image = ResizedImageField(
        size=(400, None), quality=75, upload_to='tracker/', force_format='WEBP', blank=False, null=False
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.title} ({self.date})"