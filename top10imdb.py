"""
An example script for webscrapping using python requests and regex modules

This scripts opens the imdb top movies page and fetches list of movies and prints them

Optionally, Will be implemented to store those records in sqlite database and to a csv file

"""

import requests
import re
import sys
from pprint import pprint

try:
    r = requests.get("https://www.imdbtestcom/chart/top/")
    print(dir(r))
    for header in sorted(r.headers):
        print("{} : {}".format(header, r.headers[header]))
except:
    print("Failed to fetch the imdb top movies page\nexiting...")
    sys.exit(1)

print(r.ok)

tbody = re.search(r"<tbody class=\"lister-list\">(.*)</tbody>", r.text, re.M|re.S|re.I)
tbody_html = tbody.group(1)
tr_pattern = "<tr>(.*?)</tr>"
compiled_tr_pattern = re.compile(tr_pattern, re.M|re.I|re.S)

for tr in compiled_tr_pattern.finditer(tbody_html):
    tr_html = tr.group(1)
    title = re.search(r"<td class=\"titleColumn\">.*?<a.*?>(.*?)</a>.*?<span class=\"secondaryInfo\">(.*?)</span>.*?<td class=\"ratingColumn imdbRating\">.*?<strong.*?>(.*?)</strong>", tr_html, re.M|re.S|re.I)
    title_text = title.group(1)
    release_year = title.group(2)
    rating = title.group(3)
    print("{} {}, {}".format(title_text, release_year, rating))

#pprint(r.text.split("\n"))
