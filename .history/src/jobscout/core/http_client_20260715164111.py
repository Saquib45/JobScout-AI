from __future__ import annotations

import httpx

from jobscout.core.constants import REQUEST_TIMEOUT


class HttpClient:
    """Reusable HTTP client for all scrapers."""

    def __init__(self) -> None:
        self.client = httpx.Client(
            timeout=REQUEST_TIMEOUT,
            follow_redirects=True,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/138.0 Safari/537.36"
                )
            },
        )

    def get(self, url: str) -> str:
        response = self.client.get(url)
        response.raise_for_status()
        return response.text

    def close(self) -> None:
        self.client.close()

    def __enter__(self) -> "HttpClient":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()