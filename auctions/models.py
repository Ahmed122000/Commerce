from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone



class User(AbstractUser):
    pass

    def __str__(self):
        return f"name: {self.first_name} {self.last_name}".strip()

class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='auctions/', blank=True, null=True)
    category = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings') 
    active = models.BooleanField(default=True)
    watchers = models.ManyToManyField(User, blank=True, related_name="watchlist_listings")

    def __str__(self):
        return f"{self.title} (${self.current_price})"
    
    def save(self, *args, **kwargs):
        if not self.current_price: 
            self.current_price = self.starting_bid
        super().save(*args, **kwargs)


class Bid(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"${self.amount} on {self.listing} by  {self.bidder.username}"


class Comment(models.Model):
    content = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    created_at = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"comment by {self.author.username} on {self.listing.title}"
