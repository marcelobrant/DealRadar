"""Core data models for DealRadar."""

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Listing:
    """A marketplace listing tracked by DealRadar."""

    title: str
    price: Decimal
    url: str
    marketplace: str
