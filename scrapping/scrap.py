import urllib.request
from bs4 import BeautifulSoup


url = input("Enter URL: ")

# Read HTML of URL
html = urllib.request.urlopen(url).read()

# parsing HTML
soup = BeautifulSoup(html, "html.parser")

# initialize counting and sum
total = 0
count = 0

# find tags <span>
tags = soup('span')
for tag in tags:
    # Extract and convert to int
    total += int(tag.contents[0])
    count += 1

# Show COunt and sum
print("Count", count)
print("Sum", total)
