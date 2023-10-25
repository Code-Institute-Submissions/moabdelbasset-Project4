from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField
from .services import fetch_calories
from profiles.models import Profile

# Create your models here.


class Tracker(models.Model):
    """ "
    A model for calories tracker
    """

    MEAL_CHOICES = (
        ("Breakfast", "Breakfast"),
        ("Lunch", "Lunch"),
        ("Dinner", "Dinner"),
        ("Snack", "Snack"),
    )

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="trackers")
    title = models.CharField(max_length=300, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    portion_size = models.CharField(max_length=200, blank=False, null=False)
    meal_type = models.CharField(choices=MEAL_CHOICES, max_length=10, default="Snack")
    calories = models.FloatField(null=False, default="0")
    image = ResizedImageField(
        size=(400, None),
        quality=75,
        upload_to="tracker/",
        force_format="WEBP",
        blank=True,
        null=False,
    )
    image_alt = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.title} ({self.date})"

    def save(self, *args, **kwargs):
        if not self.calories:
            self.calories = fetch_calories(self.title, self.portion_size)
        super().save(*args, **kwargs)
