from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .forms import ListingForm
from .models import User, Listing, Category, Bid
from django.utils import timezone


def index(request):
    return render(request, "auctions/index.html", {
        'header': "Active Listings", 
        'listings':Listing.objects.filter(end_time__gt=timezone.now())
        }
    )

def get_item(request, id):
    item = Listing.objects.get(id=id)
    return render(request, "auctions/item.html", {
        "listing": item
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def add_new_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = request.user
            listing.current_price = listing.starting_bid
            listing.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'auctions/new_listing.html', {
                'form':form
                }
            )
    else: 
        return render(request, 'auctions/new_listing.html', {
            "form": ListingForm()
        })
    
@login_required
def categories(request):
    return render(request, 'auctions/categories.html', {
        'categories': Category.objects.all()
        }
    )

def list_category(request, category):
    return render(request, "auctions/index.html", {
        'header': category, 
        'listings':Listing.objects.filter(category__name = category)
        }
    )

@login_required
def place_bid(request, item_id):
    if request.method == 'POST':
        bid_amount = request.POST['bid_amount']
        listing = Listing.objects.get(id=item_id)
        bidder = request.user
        
        try:
            bid_amount = float(bid_amount)
            if bid_amount <= listing.current_price:
                messages.error(request, "Bid must be higher than current price")
                return redirect('item', id=item_id)

            bid = Bid.objects.create(amount = bid_amount, listing = listing, bidder = bidder)
            bid.save()

            messages.success(request, "Bid placed succeessfully")
            return redirect('item', id=item_id)
        except(ValueError, TypeError):
            messages.error(request, "Invalid bid amount")
            return redirect('item', id=item_id)

    return redirect('item', id=item_id)
        

@login_required
def watchlist(request):
    if not request.user.is_authenticated:
        return render(request, 'auctions/login.html')
    
    return render(request, 'auctions/index.html', {
        'header':"watchlist", 
        "listings": request.user.watchlist_listings.all()
    })