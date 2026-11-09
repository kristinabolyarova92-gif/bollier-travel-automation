
import requests
from bs4 import BeautifulSoup

url = "https://travel.bolliereventsgroup.com/kalendar/ekskurzii-i-pochivki-noemvri/11"

try:
    response = requests.get(
        url,
        timeout=30,
        headers={"User-Agent": "Mozilla/5.0"}
    )
    print("HTTP status:", response.status_code)
print("Response headers:", dict(response.headers))
print("Response preview:", response.text[:500])
response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()

    text = soup.get_text(" ", strip=True)

    print("HTTP status:", response.status_code)
    print("Page title:", soup.title.get_text(strip=True) if soup.title else "None")
    print("Text length:", len(text))
    print("First 3000 characters:")
    print(text[:3000])

except requests.RequestException as error:
    print("ERROR:", error)
    raise
