import time
import requests

from bs4 import BeautifulSoup
from .headers import get_realistic_headers
from .cache import load_from_cache, save_to_cache
from .session import create_session

SCRAPE_DELAY_SECONDS = 1 

# Persistent session for scraping
session = create_session()

def scrape(url: str) -> BeautifulSoup:
    """
    Fetches and parses a web page using a shared session, caching all responses
    
    Args:
        url (str): The URL to scrape.
        
    Returns:
        BeautifulSoup: Parsed HTML content of the page.
    """
    cached_html = load_from_cache(url)
    if cached_html:
        return BeautifulSoup(cached_html, "html.parser")
    
    response = session.get(url, timeout=session.request_timeout)
    response.raise_for_status()
    
    html = response.text
    save_to_cache(url, html)
    
    time.sleep(SCRAPE_DELAY_SECONDS)
    return BeautifulSoup(html, "html.parser")