import requests
from bs4 import BeautifulSoup

def scrape_timesjobs(role, location):
    url = (
        "https://www.timesjobs.com/candidate/job-search.html"
        f"?searchType=personalizedSearch&txtKeywords={role}&txtLocation={location}"
    )

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    jobs = []
    cards = soup.select("li.clearfix.job-bx")

    for c in cards[:10]:
        # Title
        title_tag = c.h2
        title = title_tag.text.strip() if title_tag else ""

        # Company
        company_tag = c.select_one("h3 span")
        company = company_tag.text.strip() if company_tag else ""

        # Location
        loc_tag = c.select_one("ul li span")
        loc = loc_tag.text.strip() if loc_tag else location

        # Posted
        posted_tag = c.select_one("span.sim-posted")
        posted = posted_tag.text.strip() if posted_tag else ""

        # Link
        link_tag = c.h2.a if c.h2 else None
        link = link_tag["href"] if link_tag else ""

        jobs.append({
            "title": title,
            "company": company,
            "location": loc,
            "salary": None,
            "link": link,
            "platform": "TimesJobs",
            "posted": posted
        })

    return jobs
