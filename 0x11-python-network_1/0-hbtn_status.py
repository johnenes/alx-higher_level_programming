#!/usr/bin/python3
"""
    Script that fetch https://alx-intranet.hbtn.io/status
    using urllib
"""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    html = response.read().decode('utf-8')
print("Body response:")
print("\t- type: {} ".format(type(html)))
print("\t- content: {} ".format(html))
