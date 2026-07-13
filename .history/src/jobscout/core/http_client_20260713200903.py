from __future__ import annotations

import requests


class HttpClient:

    def __init__(self):
        self.session = requests.Session()

        self.session.headers.update(
            {
                "User-Agent":
                "JobScoutAI/1.0 (+https://github.com/Saquib45/JobScout-AI)"
            }
        )

    def get(self, url: str) -> str:

        response = self.session.get(
            url,
            timeout=20
        )

        response.raise_for_status()

        return response.text