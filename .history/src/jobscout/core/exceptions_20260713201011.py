class JobScoutError(Exception):
    """Base exception."""


class ScraperError(JobScoutError):
    """Scraper failed."""


class DatabaseError(JobScoutError):
    """Database failed."""


class NotificationError(JobScoutError):
    """Notification failed."""