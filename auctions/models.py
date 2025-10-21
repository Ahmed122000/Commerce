from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone



class User(AbstractUser):
    def __str__(self):
        return f"name: {self.username}".strip()

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='listing_images/', blank=True, null=True)
    category = models.ManyToManyField(Category, blank=True, related_name='listings')
    created_at = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings') 
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="won_listings")
    watchers = models.ManyToManyField(User, blank=True, related_name="watchlist_listings")
    
    def __str__(self):
        return f"{self.title} (${self.current_price})"
    
    def save(self, *args, **kwargs):
        if not self.current_price: 
            self.current_price = self.starting_bid
        super().save(*args, **kwargs)

    @property
    def highest_bid(self):
        return self.bids.order_by('-amount').first()
    
    @property
    def is_active(self):
        return self.end_time > timezone.now()
            

class Bid(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-amount']

    def __str__(self):
        return f"${self.amount} on {self.listing} by  {self.bidder.username}"


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.amount > self.listing.current_price:
            self.listing.current_price = self.amount
            self.listing.save()

class Comment(models.Model):
    content = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ['-created_at']

    def __str__(self):
        return f"comment by {self.author.username} on {self.listing.title}"

