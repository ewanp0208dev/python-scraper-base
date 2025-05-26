from infrastructure.scraper import scrape
from infrastructure.logger import logger

logger.info("Scraping transfermarkt")
soup = scrape("https://www.transfermarkt.co.uk/chelsea/startseite/verein/985/saison_id/2024")