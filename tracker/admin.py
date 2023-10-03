from django.contrib import admin
from .models import Tracker
# Register your models here.


@admin.register(Tracker)
class TrackerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'calories',
        'date',
        'image'
    )
    list_filter = ('meal_type',)