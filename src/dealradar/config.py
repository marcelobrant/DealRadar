"""Configuration for DealRadar."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Runtime settings for the marketplace monitor."""

    request_timeout: int = 15
    user_agent: str = "DealRadar/0.1.0"


settings = Settings()
