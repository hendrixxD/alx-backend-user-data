import requests

# get request
r = requests.get('http://api.github.com/events')

# post request
r = requests.post('https://httpbin.org/post', data={'key': 'value'})

# PUT request
r = requests.put('https://httpbin.org/put', data={'key': 'value'})

# DELETE request
r = requests.delete('https://httpbin.org/delete')

# HEAD request
r = requests.head('https://httpbin.org/get')

# OPTIONS request
r = requests.options('https://httpbin.org/get')

# Passing Parameters in URLs
payload = {"key1": 'val1', 'key2': 'val2'}
re = requests.get('https://httpbin.org/get', params=payload)

# passing a list of values
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

print(re.url)

# Response Content
re.text

# binary content
re.content

from PIL import Image
from io import BytesIO

i = Image.open(BytesIO(re.content))

# Json res content
re.json()
