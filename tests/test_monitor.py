from decimal import Decimal

from dealradar.models import Listing
from dealradar.monitor import filter_by_max_price


def test_filter_by_max_price():
    listings = [
        Listing("Cheap item", Decimal("25.00"), "https://example.com/1", "Example"),
        Listing("Expensive item", Decimal("100.00"), "https://example.com/2", "Example"),
    ]

    results = filter_by_max_price(listings, Decimal("50.00"))

    assert len(results) == 1
    assert results[0].title == "Cheap item"
