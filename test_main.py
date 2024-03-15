from urlshort import create_app


def test_shorten(client):
    response = client.get("/")
    assert b"Shorten" in response.data
    # assert b"URL to Shorten" in response.data
    # assert b"Short Name" in response.data
    # assert b"Shorten" in response.data
    # assert b"Your Shorteneflaskd URL" not in response.data
    # assert b"Your Shortened File" not