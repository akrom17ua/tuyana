from django.db import models
from django.conf import settings
from catalog.models import Listing, ListingImage


class Review(models.Model):
    "A user submitte review"
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveSmallIntegerField(default=0, help_text="Rating on a scale of 1 to 5")
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        #Ensure that each user can post only one review per listing
        unique_together = ('user', 'listing')
        
    def __str__(self):
        return f"Review of {self.listing} by {self.user} - {self.rating} starts"
    
    #also need to calculate average rating later
    
    
class ImageLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="image_likes")
    listing_image = models.ForeignKey(ListingImage, on_delete=models.CASCADE, related_name="likes")
    number_of_likes = models.IntegerField()
    
    class Meta:
        unique_together = ('user', 'listing_image') 
        
    def __str__(self):
        return self.listing_image.like_count
        
        
class ImageComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="image_comments")
    listing_image = models.ForeignKey(ListingImage, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} - {self.comment}"