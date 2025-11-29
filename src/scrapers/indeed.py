import requests
from bs4 import BeautifulSoup

def scrape_indeed(role, location):
    url = f"https://in.indeed.com/jobs?q={role}&l={location}"
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    jobs = []

    cards = soup.select("div.cardOutline")

    for c in cards[:10]:
        title_tag = c.select_one("h2 span")
        company_tag = c.select_one("span.companyName")
        loc_tag = c.select_one("div.companyLocation")
        salary_tag = c.select_one("div.salary-snippet")

        title = title_tag.text.strip() if title_tag else ""
        company = company_tag.text.strip() if company_tag else ""
        loc = loc_tag.text.strip() if loc_tag else ""
        salary = salary_tag.text.strip() if salary_tag else None

        link_tag = c.find("a", href=True)
        link = "https://in.indeed.com" + link_tag["href"] if link_tag else ""

        jobs.append({
            "title": title,
            "company": company,
            "location": loc,
            "salary": salary,
            "link": link,
            "platform": "Indeed",
            "posted": None
        })

    return jobs
