from bs4 import BeautifulSoup
import requests

from util.paths import ROOT_PATH


class SubpathScraper:

    def __init__(self, objects_subpath):
        self.objects_subpath = objects_subpath

    def scrape_subpaths(self):
        html = requests.get(ROOT_PATH + self.objects_subpath).content
        soup = BeautifulSoup(html, "lxml")
        data = soup.find("table", {"class": "navbox hlist collapsible"}).find_all("li")
        subpaths = set()

        for entry in data:
            subpath = entry.find("a")
            if subpath and '#' not in subpath.get("href"):
                subpaths.add(subpath.get("href"))

        return subpaths
