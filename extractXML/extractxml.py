import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# Get URL
url = input('Enter location: ')
print('Retrieving', url)

# Read URL
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

# Analyse XML
tree = ET.fromstring(data)

# Extract, coun and sum
counts = tree.findall('.//count')
total = sum(int(count.text) for count in counts)

# print results
print('Count:', len(counts))
print('Sum:', total)
