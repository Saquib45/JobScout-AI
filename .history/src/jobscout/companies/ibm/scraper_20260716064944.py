from jobscout.companies.base_scraper import BaseScraper
from jobscout.models.job import Job


class IBMScraper(BaseScraper):

    @property
    def company_name(self) -> str:
        return "IBM"

    @property
    def careers_url(self) -> str:
        return "https://www.ibm.com/careers/search"

    def scrape(self) -> list[Job]:
        return []