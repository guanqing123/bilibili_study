import requests

url = ''
resp = requests.get(url)
open('美少女战士.mp4,' 'wb').write(resp.content)