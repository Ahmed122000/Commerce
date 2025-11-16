from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_listing", views.add_new_listing, name='new_listing'),
    path("listing/<int:id>", views.get_item, name="item"),
    path("categories", views.categories, name="categories"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("categories/<str:category>", views.list_category, name="category"),
    path("place_bid/<int:item_id>", views.place_bid, name='place_bid'),
    path("toggle", views.toogle_watchlist, name='toggle_watchlist'),
    path("end_auction", views.close_auction, name='end_auction' )
]
