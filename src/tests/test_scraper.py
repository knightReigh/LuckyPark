# test_scraper.py

import pytest
from scraper import scraper


URLs = [
        "https://www.google.com",
        "https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States",
        "https://www.nationalpark-adventures.com/united-states-national-parks.html",
        "https://www.nps.gov/findapark/index.htm",
        "https://www.googl.com"
        ]

@pytest.mark.parametrize("uri", URLs)
def test_http(uri):
    assert scraper.requestHTTP(uri) != None, "Connection failed for " + uri
