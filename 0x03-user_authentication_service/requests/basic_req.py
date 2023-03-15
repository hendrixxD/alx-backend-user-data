#!/usr/bin/env python3

import requests

r = requests.get('https://api.github.com/events', stream=True)
print(r.raw)
r.raw.read(10)

with open(filename, 'wb') as fd:
    for chunk in iter_content(chunk_size=128):
        fd.write(chunk)

#  An important note about using Response.
# iter_content versus Response.raw.
# Response.iter_content will automatically
# decode the gzip and deflate transfer-encodings.
# Response.raw is a raw stream of bytes –
# it does not transform the response content. 
# If you really need access to the bytes as
# they were returned, use Response.raw.