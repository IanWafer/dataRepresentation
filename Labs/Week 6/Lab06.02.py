import requests
import json

apiKey = '4dc1bcd1ccb18bd53739d910a5c68c3fd439b2ad'
url = 'https://api.github.com/IanWafer/datarepresentationstudent-aPrivateOne'
data = {'apiKey': apiKey}
#response = requests.post(url, json=data)
#print (response.status_code)
#newFile = open("lab06.02.01.htmlaspdf.pdf", "wb")
#newFile.write(response.content)

filename = "repo.json"
response = requests.get(url, auth=('token',apiKey))
repoJSON = response.json()
#print (response.json())
file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)