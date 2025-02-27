from django.db import models

from django.conf import settings
from catalog.models import Listing

ORDER_STATUS_CHOICES = (
    ('PENDING', 'Pending'),
    ('PAID', 'Paid'),
    ('SHIPPED', 'Shipped'),
    ('COMPLETED', 'Completed'),
    ('CANCELLED', 'Cancelled'),
)

class Order(models.Model):
    """
    Represents a purchase order for one or more product-type listings.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=ORDER_STATUS_CHOICES, default = 'PENDING')
    total_amount = models.DecimalField(max_digits = 10 , decimal_places = 2, default = 0)
    shipping_address = models.CharField(max_length = 255, blank = True, null = True)
    # Alternatively, link to the Address model: shipping_address = models.ForeignKey(Address, ...)
    
    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"
    
class OrderItem(models.Model):
    """
    Line item in an Order. Each item references a Listing of type PRODUCT.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    listing = models.ForeignKey(Listing, on_delete=models.SET_NULL, null=True, related_name = "order_items")
    quantity = models.PositiveIntegerField(default = 0)
    price = models.DecimalField(max_digits = 10, decimal_places=2)
    
    def __str__(self):
       return f"{self.quantity} x {self.listing.title if self.listing else 'Deleted Listing'}"
    
    