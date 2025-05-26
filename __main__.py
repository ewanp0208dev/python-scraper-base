from infrastructure.scraper import scrape
from infrastructure.logger import logger


def main():
    soup = scrape("https://www.example.com")
    logger.info(soup)


if __name__ == '__main__':
    main()