from abc import ABC, abstractmethod

from jobscout.models.job import Job


class BaseScraper(ABC):
    """
    Abstract base class for all company scrapers.
    """

    company_name: str

    @abstractmethod
    def fetch_jobs(self) -> list[Job]:
        """
        Return all available jobs.
        """
        raise NotImplementedError