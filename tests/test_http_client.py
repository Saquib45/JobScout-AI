from jobscout.core.http_client import HttpClient


def test_google():
    with HttpClient() as client:
        html = client.get("https://example.com")
        assert "Example Domain" in html