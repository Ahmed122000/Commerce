def get_active_listings(items):
    active = [listing for listing in items if listing.is_active]

    return active 