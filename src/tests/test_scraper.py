# test_scraper.py

import pytest
import re
from scraper import scraper


## Test Http request ##
URLs = [
        "https://www.google.com",
        "https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States",
        "https://www.nationalpark-adventures.com/united-states-national-parks.html",
        "https://www.nps.gov/findapark/index.htm",
        "https://www.googl.com"
        ]

@pytest.mark.parametrize("uri", URLs)
def test_http(uri):
    print("Validate: " + uri)
    assert scraper.requestHTTP(uri) != None, "Connection failed for " + uri

URLs = [
        ("https://www.google.com", "https://www.google.com"),
        ("www.163.com", "http://www.163.com"),
        ("http://www.163.com", "http://www.163.com"),
        ("http://localhost", "http://localhost"),
        ("ftps:1231.com", "http://ftps:1231.com")
        ]

## Test URL validation ##
@pytest.mark.parametrize("uri, expected", URLs)
def test_validateurl(uri, expected):
    assert scraper.validateURL(uri) == expected, uri + "validation failed"
