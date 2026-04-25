# 🏆 Commerce - Django Auction Platform

[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.2+-green?style=flat-square&logo=django)](https://djangoproject.com)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.0-purple?style=flat-square&logo=bootstrap)](https://getbootstrap.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

A full-featured **eBay-style auction platform** built with **Django** where users can create, bid on, and manage auction listings in real-time. Created as **Project 2** for Harvard's CS50 Web Development course.

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation--setup)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Database Models](#-database-models)
- [API Endpoints](#-api-endpoints)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### 🛍️ Core Auction Functionality
- **📝 Create Listings**: Users can create new auction listings with:
  - Title, description, starting bid
  - Image upload support
  - Category selection
  - Detailed product information

- **🏷️ Active Listings**: Browse all currently active auctions with:
  - Real-time price updates
  - Current bidder information
  - Time remaining display
  - Bid history

- **💰 Bidding System**:
  - Place bids with automatic validation
  - Minimum bid enforcement
  - Bid outbidding notifications
  - Real-time bid counter

- **📌 Watchlist Management**:
  - Add/remove listings from personal watchlist
  - Quick access to tracked items
  - Watchlist notifications for price changes
  - Bidding reminders

### 🏷️ Categories & Organization
- **Category System**: Organize listings by categories:
  - Fashion & Accessories
  - Electronics & Technology
  - Home & Garden
  - Sports & Outdoors
  - Toys & Games
  - Books & Media
  - Art & Collectibles

- **Smart Filtering**: Filter and search listings by:
  - Category
  - Price range
  - Auction status
  - Most popular

### 👥 User Features
- **🔐 Authentication**:
  - Secure user registration
  - Login/logout functionality
  - Password management
  - Session security

- **📊 Personal Dashboard**:
  - Manage created listings
  - Track active bids
  - View bidding history
  - Watchlist overview

- **🎯 Auction Management**:
  - Close your own auctions
  - Declare winners
  - Re-list closed auctions
  - Mark items as sold

- **💬 Comment System**:
  - Add comments to listings
  - Discuss with other bidders
  - Seller responses
  - Comment history

### ⚡ Real-time Updates
- **📈 Current Price Tracking**: Automatic updates with new bids
- **🔄 Auction Status**: Live tracking of active/ended auctions
- **🏆 Winner Declaration**: Automatic assignment when auctions close
- **🔔 Notifications**: Email/in-app notifications for bidding activity

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend Framework** | Django 4.2+ |
| **Language** | Python 3.8+ |
| **Frontend** | HTML5, CSS3, Bootstrap 5 |
| **Database** | SQLite (Development), PostgreSQL (Production) |
| **ORM** | Django ORM |
| **Authentication** | Django auth system |
| **Forms** | Django Forms |
| **Admin Panel** | Django Admin |

---

## 🚀 Installation & Setup

### Prerequisites
- **Python 3.8** or higher
- **pip** (Python package manager)
- **Git** for cloning
- Virtual environment (recommended)

### Step-by-Step Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Ahmed122000/Commerce.git
   cd Commerce
   ```

2. **Create virtual environment**:
   ```bash
   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   
   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create `.env` file** (optional):
   ```bash
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. **Apply migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser** (admin account):
   ```bash
   python manage.py createsuperuser
   # Follow prompts to create admin account
   ```

7. **Collect static files** (optional):
   ```bash
   python manage.py collectstatic --noinput
   ```

8. **Run development server**:
   ```bash
   python manage.py runserver
   ```

9. **Access the application**:
   ```
   Application: http://localhost:8000
   Admin Panel: http://localhost:8000/admin
   ```

---

## 💡 Usage

### For Buyers
1. **Browse Listings**:
   - Visit homepage to see active auctions
   - Use categories to filter items
   - Search for specific products

2. **Place a Bid**:
   - Click on a listing to view details
   - Enter bid amount (must exceed current bid)
   - Click "Place Bid" to bid

3. **Manage Watchlist**:
   - Click heart icon to add to watchlist
   - View watchlist from profile
   - Get notified on bid activity

4. **View Comments**:
   - Scroll to comments section on listing page
   - Add your own comments for discussion

### For Sellers
1. **Create Listing**:
   - Click "Create Listing" button
   - Fill in all required information
   - Upload product image
   - Set starting bid and category
   - Click "Create" to list

2. **Manage Active Auctions**:
   - View current bids on dashboard
   - Monitor bidding activity
   - Track auction time remaining

3. **Close Auction**:
   - Click "Close Auction" when done
   - Winner is automatically determined
   - Item marked as sold

4. **Respond to Comments**:
   - View buyer comments on your listings
   - Respond to questions

---

## 📂 Project Structure

```plaintext
Commerce/
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── db.sqlite3                   # SQLite database
├── commerce/                    # Main project directory
│   ├── settings.py             # Django settings
│   ├── urls.py                 # URL configuration
│   ├── asgi.py                 # ASGI config
│   └── wsgi.py                 # WSGI config
├── auctions/                    # Main app directory
│   ├── migrations/             # Database migrations
│   ├── static/auctions/
│   │   ├── css/
│   │   │   └── styles.css      # Custom styling
│   │   └── js/
│   │       └── script.js       # JavaScript logic
│   ├── templates/auctions/
│   │   ├── layout.html         # Base template
│   │   ├── index.html          # Homepage
│   │   ├── listing.html        # Single listing
│   │   ├── new_listing.html    # Create listing form
│   │   ├── categories.html     # Categories page
│   │   ├── watchlist.html      # Watchlist
│   │   ├── login.html          # Login page
│   │   ├── register.html       # Registration page
│   │   └── error.html          # Error page
│   ├── models.py               # Database models
│   ├── views.py                # Application logic
│   ├── urls.py                 # App URL routing
│   ├── forms.py                # Django forms
│   ├── admin.py                # Admin configuration
│   └── apps.py                 # App configuration
└── README.md                   # This file
```

---

## 🗃️ Database Models

### User Model
```python
class User(AbstractUser):
    # Extends Django's default User model
    pass
```

### Category Model
```python
class Category(models.Model):
    name = CharField(max_length=64, unique=True)
    description = TextField(blank=True)
```

### Listing Model
```python
class Listing(models.Model):
    title = CharField(max_length=200)
    description = TextField()
    starting_price = DecimalField(max_digits=10, decimal_places=2)
    current_price = DecimalField(max_digits=10, decimal_places=2)
    image_url = URLField(blank=True)
    category = ForeignKey(Category, on_delete=CASCADE)
    creator = ForeignKey(User, on_delete=CASCADE)
    is_active = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)
    closed_at = DateTimeField(null=True, blank=True)
    winner = ForeignKey(User, null=True, related_name='won_auctions')
```

### Bid Model
```python
class Bid(models.Model):
    listing = ForeignKey(Listing, on_delete=CASCADE)
    bidder = ForeignKey(User, on_delete=CASCADE)
    amount = DecimalField(max_digits=10, decimal_places=2)
    timestamp = DateTimeField(auto_now_add=True)
```

### Comment Model
```python
class Comment(models.Model):
    listing = ForeignKey(Listing, on_delete=CASCADE)
    author = ForeignKey(User, on_delete=CASCADE)
    content = TextField()
    timestamp = DateTimeField(auto_now_add=True)
```

### Watchlist Model
```python
class Watchlist(models.Model):
    user = ForeignKey(User, on_delete=CASCADE)
    listing = ForeignKey(Listing, on_delete=CASCADE)
    added_at = DateTimeField(auto_now_add=True)
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Homepage - all active listings |
| `GET` | `/listing/<id>` | View single listing |
| `POST` | `/listing/create` | Create new listing |
| `POST` | `/listing/<id>/bid` | Place a bid |
| `POST` | `/listing/<id>/close` | Close auction |
| `GET` | `/categories` | View all categories |
| `GET` | `/category/<name>` | View listings by category |
| `GET` | `/watchlist` | View user's watchlist |
| `POST` | `/listing/<id>/watchlist` | Add to watchlist |
| `POST` | `/comment/<id>` | Add comment |
| `GET` | `/search` | Search listings |
| `GET` | `/login` | Login page |
| `GET` | `/register` | Registration page |
| `POST` | `/logout` | Logout user |

---

## 🎨 Features in Detail

### Bidding Logic
- Validates bid amount against current highest bid
- Prevents users from bidding on own listings
- Automatic winner declaration
- Bid history tracking

### Watchlist System
- One-click add/remove
- Quick access to tracked items
- Persistent across sessions
- Bid notifications

### Category Organization
- Hierarchical category structure
- Filter by category on homepage
- Category browsing page

### Search Functionality
- Full-text search across listings
- Search by title, description, or category
- Partial match suggestions

---

## 🧪 Testing

Run tests with:
```bash
python manage.py test auctions
```

---

## 🐛 Known Issues & Limitations

- Email notifications not yet implemented
- Real-time updates require page refresh
- Image handling could be improved with CDN

---

## 🚀 Future Enhancements

- [ ] Real-time bidding with WebSockets
- [ ] Email notifications
- [ ] Advanced search with filters
- [ ] User ratings and reviews
- [ ] Payment integration (Stripe)
- [ ] Mobile app version
- [ ] API for third-party integration

---

## 📝 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 🙌 Acknowledgments

- Harvard's CS50 Web course for project specification
- Django documentation and community
- Bootstrap team for CSS framework
- All contributors and testers

---

## 📞 Support

Have questions or found bugs? Open an issue on GitHub!

**Repository**: [Ahmed122000/Commerce](https://github.com/Ahmed122000/Commerce)

---

**Last Updated**: April 2026 | Built with ❤️ by Ahmed Hesham
