import re
import requests
import csv
from bs4 import BeautifulSoup

URL = "https://www.topuniversities.com/where-to-study/north-america/united-states/ranked-top-100-us-universities"
final_data = []
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
#print(soup)
#for link in soup.find_all(string=re.compile("University")):

get_data = soup.find_all(string=re.compile("University"))
#print(get_data)

for link in get_data:
    gen_list = []
    gen_list.append(link)
    final_data.append(gen_list)
print(final_data)

with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter = ',')
    writer.writerow("")
    for i in range(0, len(final_data)):
        writer.writerow(final_data[i])

