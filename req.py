import requests
# gets webpage
res = requests.get('http://www.meteo-geneve.ch/')

# checks if status code is equal to OK (HTML 200)
res.status_code == requests.codes.ok

# turns it into text
print(res.text[:200])

# Other way to check status: if ok, nothing happens, if not, halts
res.raise_for_code()

# example

try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
