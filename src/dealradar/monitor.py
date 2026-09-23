"""Marketplace monitoring logic."""

from collections.abc import Iterable

from .models import Listing


def filter_by_max_price(
    listings: Iterable[Listing], max_price
) -> list[Listing]:
    """Return listings priced at or below max_price."""
    return [listing for listing in listings if listing.price <= max_price]
