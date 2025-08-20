from app.main import fetch_html, extract_title


def test_extract_title_ok():
    html = """
        <html>
          <head><title>Example Domain</title></head>
          <body><h1>Hi</h1></body>
        </html>
        """
    assert extract_title(html) == "Example Domain"


def test_extract_title_none():
    html = "<html><head></head><body>No title here</body></html>"
    assert  extract_title(html) is None


def test_fetch_html_monkeypatch(monkeypatch):
    class DummyResponse:
        status_code = 200
        text = "<title>Fake</title>"
        def raise_for_status(self): pass

    def fake_get(url, timeout=10):
        return DummyResponse()

    import requests
    monkeypatch.setattr(requests, "get", fake_get)
    html = fetch_html("https://example.com")
    assert "Fake" in html
