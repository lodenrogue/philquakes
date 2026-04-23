import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://earthquake.phivolcs.dost.gov.ph/"

response = requests.get(base_url, verify=False)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

print("url,date - time,(philippine time),latitude,(ºn),longitude,(ºe),depth,(km),mag,location")

for table in soup.select('.MsoNormalTable')[2:3]:
    for row in table.select('tr'):
        if not row.find('td'):
            continue
            
        link_tag = row.find('a')
        link = ""
        if link_tag:
            # Prepend base URL and replace extension
            link = base_url + link_tag['href'].replace(".html", ".jpg")
        
        cells_text = row.get_text(",", strip=True)
        
        if cells_text:
            print(f"{link},{cells_text}")
