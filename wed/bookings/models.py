from django.db import models

from django.conf import settings
from catalog.models import Listing

BOOKING_STATUS_CHOICES = (
    ('PENDING', 'Pending'),
    ('CONFIRMED', 'Confirmed'),
    ('CANCELLED', 'Cancelled'),
)

class Booking(models.Model):
    """
    Represents a user booking a listing (service or venue) for specific dates.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True) #optional if single day
    number_of_guests = models.PositiveIntegerField(blank = True, null = True, help_text="Only for capacity based listings")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default = 0)
    status = models.CharField(max_length=10, choices = BOOKING_STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Booking {self.id} by {self.user.username} for {self.listing.title}"
    
    
    
