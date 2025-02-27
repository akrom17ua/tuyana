from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length = 30, blank = True)
    is_vendor = models.BooleanField(default = False)
    
    def __str__(self):
        return self.username
    
    
class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="vendor_profile")
    business_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank = True)
    #Futher things will be added
    
    def __str__(self):
        return self.business_name
    

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    street = models.CharField(max_length= 250)
    city = models.CharField(max_length = 250)
    country = models.CharField(max_length = 250)
    
    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"