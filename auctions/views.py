from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import ListingForm
from .models import User, Listing, Category


def index(request):
    return render(request, "auctions/index.html", {'header': "Active Listings", 'listings':Listing.objects.all()})


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


def add_new_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.POST)
            print(request.FILES)
            listing = form.save(commit=False)
            listing.owner = request.user
            listing.current_price = listing.starting_bid
            listing.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'auctions/new_listing.html', {'form':form})
    else: 
        return render(request, 'auctions/new_listing.html', {
            "form": ListingForm()
        })
    

def categories(request):
    return render(request, 'auctions/categories.html', {'categories': Category.objects.all()})

def list_category(request, category):
    return render(request, "auctions/index.html", {'header': category, 'listings':Listing.objects.filter(category__name = category)})

def watchlist(request):
    pass