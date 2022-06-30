from bs4 import BeautifulSoup
import requests

from entity.block import Block
from scraper.subpath_scraper import SubpathScraper
from util.paths import BLOCKS_SUBPATH, ROOT_PATH


def scrape():
    block = Block()

    scraper = SubpathScraper(BLOCKS_SUBPATH)
    demo_url = ROOT_PATH + next(iter(scraper.scrape_subpaths()))
    html = requests.get(demo_url).content
    soup = BeautifulSoup(html, "lxml")
    data = soup.find("div", {"class": "notaninfobox"})

    block.name = soup.find("div", {"class": "mcwiki-header infobox-title"}).get_text()
    table = soup.find("table", class_="infobox-rows")
    rows = table.find_all("tr")

    for row in rows:
        print(row.get_text().strip() + "\n====\n")

    print(demo_url)
