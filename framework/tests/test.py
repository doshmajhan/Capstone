import requests
import json

print("######## Pass/Fail ########")
target = 'http://127.0.0.1:5000/api/os_list'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.get(target, headers=headers)
data = json.loads(r.text)
print(r.status_code, r.reason)
print(r.text)

print("######## Pass/Fail ########")
target = 'http://127.0.0.1:5000/api/verify'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data = {'selected_os': 'Ubuntu 16.04'}
r = requests.post(target, data=json.dumps(data), headers=headers)
data = json.loads(r.text)
print(r.status_code, r.reason)
print(r.text)