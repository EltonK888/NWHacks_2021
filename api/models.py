from django.db import models

# Create your models here.

class Venue(models.Model):
    name = models.CharField(max_length=255, blank=False, null=True)
    address = models.CharField(max_length=255, blank=False, null=True)
    theme_night = models.BooleanField(default=False, blank=False, null=True)
    people = models.PositiveIntegerField(blank=False, null=True)
    current_music = models.CharField(max_length=100, blank=False, null=True)
    average_age = models.PositiveIntegerField(blank=False, null=True)
    sound_level = models.PositiveIntegerField(default=60, validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return self.name