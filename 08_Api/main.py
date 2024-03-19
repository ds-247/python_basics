import requests

resp = requests.get('https://api.freeapi.app/api/v1/public/randomusers/user/random')

print(resp.status_code)
print(resp.headers)
print(resp.encoding)
print(resp.text)
print(resp.json())