from jobscout.core.html_parser import HTMLParser


def test_html_parser():
    html = """
    <html>
        <body>
            <h1>Hello World</h1>
        </body>
    </html>
    """

    soup = HTMLParser.parse(html)

    assert soup.h1.text == "Hello World"