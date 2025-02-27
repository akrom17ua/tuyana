from django.db import models

from users.models import Vendor

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
    
LISTING_TYPE_CHOICES = (
    ('PRODUCT', 'Product'),
    ('SERVICE', 'Service'),
    ('VENUE', 'Venue'),
)

class Listing(models.Model):
    """
    Generic model for any listing (dress, florist, venue, etc.).
    The `listing_type` determines its behavior in the booking/purchase flow.
    """
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="listings")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name = "listings")
    title = models.CharField(max_length = 255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    listing_type = models.CharField(max_length=10, choices=LISTING_TYPE_CHOICES)
    capacity = models.PositiveIntegerField(blank=True, null=True, help_text="For venues")
    city = models.CharField(max_length=255, blank=True, null=True)
    
    # Any additional fields: e.g., availability rules, location coordinates, etc.
    
    def __str__(self):
        return self.title

class ListingImage(models.Model):
    listing = models.ImageField(Listing, on_delete = models.CASCADE, related_name = "images")
    image = models.ImageField(upload_to="listing_images/")
    
    def __str__(self):
        return f"Image for {self.listing.title}"