# philquakes
# Copyright (C) 2026  Miguel Hernandez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://earthquake.phivolcs.dost.gov.ph/"

response = requests.get(base_url, verify=False)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

print("url,datetime,lat,long,depth,mag,location")

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
