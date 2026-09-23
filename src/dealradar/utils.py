"""Shared utility functions for DealRadar."""


def normalize_title(title: str) -> str:
    """Normalize whitespace in a listing title."""
    return " ".join(title.split())
