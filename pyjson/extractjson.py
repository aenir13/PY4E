import urllib.request, urllib.parse, urllib.error
import json

# get URL
url = input('Enter location: ')
print('Retrieving', url)

# read URL
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

# analyse
js = json.loads(data)

# Extract, count and sum
total = sum(int(comment['count']) for comment in js['comments'])

# print out
print('Count:', len(js['comments']))
print('Sum:', total)
