# Commerce - CS50 Web Development Project 2
## 🏆 Django Auctions - eBay-like E-commerce Auction Site

A full-featured eBay-style auction platform built with Django where users can create, bid on, and watchlist auction listings in real-time.

![Django](https://img.shields.io/badge/Django-4.2-green)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.0-purple)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)

## ✨ Features

### 🛍️ Core Auction Functionality
- **Create Listings**: Users can create new auction listings with titles, descriptions, starting bids, images, and categories
- **Active Listings**: Browse all currently active auctions with real-time pricing
- **Bid System**: Place bids with validation ensuring bids meet minimum requirements
- **Watchlist**: Add/remove listings to your personal watchlist for easy tracking

### 🏷️ Categories & Organization
- **Category System**: Listings organized by categories (Fashion, Toys, Electronics, Home, etc.)
- **Category Browsing**: Filter listings by specific categories
- **Advanced Organization**: Easy navigation through categorized listings

### 👥 User Features
- **User Authentication**: Secure registration and login system
- **Personal Dashboard**: Manage your listings, bids, and watchlist
- **Auction Management**: Close your own auctions and declare winners
- **Comment System**: Discuss listings with other users

### ⚡ Real-time Updates
- **Current Price Tracking**: Automatic price updates with new bids
- **Auction Status**: Live tracking of active/ended auctions
- **Winner Declaration**: Automatic winner assignment when auctions close

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Django 4.2+
- Pillow (for image handling)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/django-auctions.git
   cd django-auctions ```
2. ** Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate #On Windows: venv/Scripts/activate
   ```
3. **install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```  
6. Run development server
   ```bash
   python manage.py runserver
   ```
7. visit application
   ```text
   http://localhost:8000
   ```
### 📁 Project Structure

```plaintext
auctions/
├── models.py              # Database models (User, Listing, Bid, Comment, Category)
├── views.py               # Application views and business logic
├── urls.py                # URL routing configuration
├── admin.py               # Django admin interface configuration
├── forms.py               # Django forms for data validation
└── templates/             # HTML templates
    ├── auctions/
    │   ├── layout.html    # Base template
    │   ├── index.html     # Active listings page
    │   ├── item.html      # Individual listing page
    │   ├── new_listing.html # Create listing form
    │   ├── categories.html # Categories browsing
    │   ├── login.html      # User login
    │   └── register.html # User registeration
```
### 🗃️ Database Models
- **User**: Custom user model extending AbstractUser
- **Listing**: Auction items with title, description, price, image, categories
- **Bid**: Bid records with amount, bidder, and timestamp
- **Comment**: User comments on listings
- **Category**: Listing categories for organization
