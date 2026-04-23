# philquakes

Get most recent Philippines earthquake data from phivolcs

## Requirements

- `beautifulsoup4`
- `requests`

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
$ python3 philquakes.py
```

## Example Results

```
url,datetime,lat,long,depth,mag,location
https://earthquake.phivolcs.dost.gov.ph/2026_Earthquake_Information\April\2026_0423_1317_B1.jpg,23 April 2026 - 09:17 PM,14.11,120.45,070,1.8,020,km N 80° W of Nasugbu (Batangas)
https://earthquake.phivolcs.dost.gov.ph/2026_Earthquake_Information\April\2026_0423_1303_B1.jpg,23 April 2026 - 09:03 PM,07.58,124.46,005,2.3,012,km N 53° E of Buldon (Maguindanao Del Norte)
```

## Fields

- url - url of event map where earthquake occurred (.jpg format)
- datetime - date and time of the event (Philippine Time)
- lat - latitude coordinate (ºN)
- long - longitude coordinate (ºE)
- depth - depth of the earthquake in km
- mag - magnitude of the earthquake
- location - approximate geographic location of the epicenter
