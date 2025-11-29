import requests
from bs4 import BeautifulSoup

def scrape_linkedin(role, location):
    url = f"https://www.linkedin.com/jobs/search?keywords={role}&location={location}"
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    jobs = []
    cards = soup.select("div.base-card")

    for c in cards[:10]:
        title_tag = c.select_one("h3")
        company_tag = c.select_one("h4")
        loc_tag = c.select_one("span.job-search-card__location")

        title = title_tag.text.strip() if title_tag else ""
        company = company_tag.text.strip() if company_tag else ""
        loc = loc_tag.text.strip() if loc_tag else ""

        link_tag = c.find("a", href=True)
        link = link_tag["href"] if link_tag else ""

        jobs.append({
            "title": title,
            "company": company,
            "location": loc,
            "salary": None,
            "link": link,
            "platform": "LinkedIn",
            "posted": None
        })

    return jobs
