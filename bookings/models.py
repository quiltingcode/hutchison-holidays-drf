from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Booking(models.Model):
    """
    Booking model, related to User
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    booking_start_date = models.DateField(blank=False)
    booking_end_date = models.DateField(blank=False)
    length_of_stay = models.IntegerField(blank=True)
    notes = models.TextField(blank=True)
    guests = models.IntegerField(blank=False)
    cost = models.DecimalField(blank=True, decimal_places=2, max_digits=6)
    paid = models.BooleanField(blank=True, default=False)

    def save(self, *args, **kwargs):
        # Calculate and set the length_of_stay before saving
        self.length_of_stay = (self.booking_end_date - self.booking_start_date).days + 1
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner}: {self.booking_start_date} - {self.booking_end_date}'
