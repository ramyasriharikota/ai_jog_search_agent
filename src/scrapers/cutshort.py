import requests
from bs4 import BeautifulSoup

def scrape_cutshort(role, location):
    # CutShort uses SEO URLs like: https://cutshort.io/jobs/python-developer-jobs-in-Hyderabad
    formatted_role = role.replace(" ", "-")
    formatted_location = location.replace(" ", "-")

    url = f"https://cutshort.io/jobs/{formatted_role}-jobs-in-{formatted_location}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    jobs = []
    cards = soup.select("div.job-listing")

    for c in cards[:10]:
        # Title
        title_tag = c.select_one("h3")
        title = title_tag.text.strip() if title_tag else ""

        # Company
        company_tag = c.select_one(".company-name")
        company = company_tag.text.strip() if company_tag else ""

        # Location (CutShort hides it, so fallback to user input)
        loc = location

        # Link
        link_tag = c.find("a", href=True)
        link = "https://cutshort.io" + link_tag["href"] if link_tag else ""

        jobs.append({
            "title": title,
            "company": company,
            "location": loc,
            "salary": None,
            "link": link,
            "platform": "CutShort",
            "posted": None
        })

    return jobs
