import requests
from bs4 import BeautifulSoup

URL = "https://www.topuniversities.com/where-to-study/north-america/united-states/ranked-top-100-us-universities"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

print(soup)

