import requests
from bs4 import BeautifulSoup

def scrape_glassdoor(role, location):
    # Glassdoor URL pattern
    formatted_role = role.replace(" ", "-")
    formatted_location = location.replace(" ", "-")

    url = f"https://www.glassdoor.co.in/Job/{formatted_location}-{formatted_role}-jobs-SRCH_IL.0,9.htm"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    jobs = []

    # New Glassdoor markup
    cards = soup.select("li.react-job-listing")

    for c in cards[:10]:
        # TITLE
        title_tag = c.select_one("a.jobLink")
        title = title_tag.text.strip() if title_tag else ""

        # COMPANY
        company_tag = c.select_one("div.d-flex span")
        company = company_tag.text.strip() if company_tag else ""

        # Glassdoor hides location → use input
        loc = location

        # LINK
        link_tag = c.find("a", href=True)
        link = "https://www.glassdoor.co.in" + link_tag["href"] if link_tag else ""

        jobs.append({
            "title": title,
            "company": company,
            "location": loc,
            "salary": None,
            "link": link,
            "platform": "Glassdoor",
            "posted": None
        })

    return jobs
