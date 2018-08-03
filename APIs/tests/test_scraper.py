import scraper


def test_http1():
    uri = "https://pytest.readthedocs.io/en/reorganize-docs/new-docs/user/directory_structure.html"
    assert(scraper.requestHTTP(uri) != None)

