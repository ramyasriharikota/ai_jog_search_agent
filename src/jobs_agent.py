from src.scrapers.linkedin import scrape_linkedin
from src.scrapers.indeed import scrape_indeed
from src.scrapers.timesjobs import scrape_timesjobs
from src.scrapers.cutshort import scrape_cutshort
from src.scrapers.glassdoor import scrape_glassdoor

def search_all_platforms(role, location, exp):
    results = []

    try:
        results += scrape_linkedin(role, location)
    except:
        pass

    try:
        results += scrape_indeed(role, location)
    except:
        pass

    try:
        results += scrape_timesjobs(role, location)
    except:
        pass

    try:
        results += scrape_cutshort(role, location)
    except:
        pass

    try:
        results += scrape_glassdoor(role, location)
    except:
        pass

    return results[:50]
