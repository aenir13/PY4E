import urllib.request
from bs4 import BeautifulSoup

# get URL, COUNT AND POSITION
url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: ")) - 1  #Adjust possition

# repeat as many time was instructed
for i in range(count):
    print("Retrieving:", url)
    # read html of url
    html = urllib.request.urlopen(url).read()
    # parsing html
    soup = BeautifulSoup(html, "html.parser")
    # Find all the links
    tags = soup('a')
    # update URL
    url = tags[position].get('href', None)

# Show last URL recovered
print("Last URL retrieved:", url)
