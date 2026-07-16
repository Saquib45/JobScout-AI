from jobscout.companies.ibm.scraper import IBMScraper


def test_ibm_scraper():

    scraper = IBMScraper()

    assert scraper.company_name == "IBM"

    assert scraper.careers_url.startswith("https")

    assert scraper.scrape() == []