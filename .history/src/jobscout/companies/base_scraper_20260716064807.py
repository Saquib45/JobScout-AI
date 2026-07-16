from __future__ import annotations

from abc import ABC, abstractmethod

from jobscout.models.job import Job


class BaseScraper(ABC):
    """Abstract base class for all company scrapers."""

    @property
    @abstractmethod
    def company_name(self) -> str:
        """Company name."""
        ...

    @property
    @abstractmethod
    def careers_url(self) -> str:
        """Careers page URL."""
        ...

    @abstractmethod
    def scrape(self) -> list[Job]:
        """Return all discovered jobs."""
        ...