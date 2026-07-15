from bs4 import BeautifulSoup


class HTMLParser:
    """Reusable HTML parser."""

    @staticmethod
    def parse(html: str) -> BeautifulSoup:
        return BeautifulSoup(html, "lxml")