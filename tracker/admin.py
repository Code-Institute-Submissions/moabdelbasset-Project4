from django.contrib import admin
from .models import Tracker
# Register your models here.


@admin.register(Tracker)
class TrackerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'date',
        'title',
        'portion_size',
        'calories',
    )
    list_filter = ('meal_type',)