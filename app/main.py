from bs4 import BeautifulSoup
import requests


def fetch_html(url: str, timeout: int = 10) -> str:
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.text


def extract_title(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    tag = soup.find("title")
    return tag.get_text(strip=True) if tag else None



if __name__ == "__main__":
    import sys
    url = sys.argv[1] if len(sys.argv) > 1 else "https://www.example.com"
    html = fetch_html(url)
    print(extract_title(html))
