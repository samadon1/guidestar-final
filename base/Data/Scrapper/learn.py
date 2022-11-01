import csv
from email.mime import image
from urllib import request
import requests
from bs4 import BeautifulSoup
import re

data = []
causes = []
default = ["Education","Physical Health","Gender Equality","Child Protection","Economic Growth","Justice and Human Rights","Food Security","Mental Health","COVID-19","Disaster Response","Climate Action","Safe Housing","Ending Abuse","Sustainable Agriculture","Ecosystem Restoration","Clean Water","Disability Rights","Refugee Rights","Wildlife Conservation","Animal Welfare","Reproductive Health","Arts and Culture","Digital Literacy","Ending Human Trafficking","Sport","Peace and Reconciliation","Racial Justice" ,"LGBTQIA+ Equality"]

site = requests.get("https://www.globalgiving.org/search/?size=25&nextPage=1&sortField=sortorder&selectedLocations=00ghana&loadAllResults=true")
soup = BeautifulSoup(site.content, 'html.parser')

cause = soup.findAll("a", text = re.compile('^(?!Ghana$).*$'))
for c in cause:
    causes.append(c.text)

causes = [x for x in causes if x in default]


for i in range(25):
    name = soup.select('div.grid-12 > a.col_inherit')[i].text.strip()
    description = soup.select('div.col_ggSecondary1Text')[i].text.strip()
    cause = causes[i]
    image = soup.findAll("a", {"data-bg":re.compile(r".*")})[i].get("data-bg")


    data.append({
        "name": name,
        "description": description,
        "cause": cause,
        "image": image
    })



keys = data[0].keys()

with open('ngos.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data)

# name = soup.select('div.grid-12 > a.col_inherit')
# description = soup.select('div.col_ggSecondary1Text')[0].text
# cause = soup.select('span.col_ggSecondary1LightText > a.col_inherit')
# image = soup.findAll("a", {"data-bg":re.compile(r".*")})[0].get("data-bg")


