import requests

r = requests.get('http://httpbin.org/')
print(r.status_code)