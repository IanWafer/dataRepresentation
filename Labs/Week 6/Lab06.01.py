import requests
import json
from xlwt import *

#url="http://127.0.0.1:5000/cars"

#response=requests.get(url)
#data=response.json()

#output to console
#print(data)

#for car in data["cars"]:
# print (car)

#other code
#save this to a file
#filename = 'cars.json'
#if filename:
 # Writing JSON data
# with open(filename, 'w') as f:
#    json.dump(data, f, indent=4)

#other code
# write to excel file
#w = Workbook()
#ws = w.add_sheet('cars')
#row = 0;
#ws.write(row,0,"reg")
#ws.write(row,1,"make")
#ws.write(row,2,"model")
#ws.write(row,3,"price")
#row += 1
#for car in data["cars"]:
# ws.write(row,0, car["reg"])
# ws.write(row,1,car["make"])
# ws.write(row,2,car["model"])
# ws.write(row,3,car["price"])
# row += 1
#w.save('cars.xls')

#dataString = {'reg':'08 C 1234','make':'Ford','model':'Galaxy','price':12324}
#url = 'http://127.0.0.1:5000/cars'
#response = requests.post(url, json=dataString)
#print (response.status_code)

#url = 'http://127.0.0.1:5000/cars/08%20C%201234'
#response = requests.delete(url)
#print (response.status_code)
#print (response.text)

#url = "https://api.github.com/users?since=100"
url = "https://api.github.com/users/andrewbeattycourseware/followers"
response = requests.get(url)
data = response.json()
#print(data)
#Get the file name for the new file to write
filename = 'githubusers.json'
with open(filename, 'w') as f:
 json.dump(data, f, indent=4)

w = Workbook()
ws = w.add_sheet('followers')
row = 0;
ws.write(row,0,"login")
ws.write(row,1,"id")
ws.write(row,2,"node_id")
ws.write(row,3,"avatar_url")
ws.write(row,4,"gravatar_id")
ws.write(row,5,"url")
ws.write(row,6,"html_url")
ws.write(row,7,"followers_url")
ws.write(row,8,"following_url")
ws.write(row,9,"gists_url")
ws.write(row,10,"starred_url")
ws.write(row,11,"subscriptions_url")
ws.write(row,12,"organizations_url")
ws.write(row,13,"repos_url")
ws.write(row,14,"events_url")
ws.write(row,15,"received_events_url")
ws.write(row,16,"type")
ws.write(row,17,"site_admin")
row += 1
for follower in data:
 ws.write(row,0,follower["login"])
 ws.write(row,1,follower["id"])
 ws.write(row,2,follower["node_id"])
 ws.write(row,3,follower["avatar_url"])
 ws.write(row,4, follower["gravatar_id"])
 ws.write(row,5,follower["url"])
 ws.write(row,6,follower["html_url"])
 ws.write(row,7,follower["followers_url"])
 ws.write(row,8, follower["following_url"])
 ws.write(row,9,follower["gists_url"])
 ws.write(row,10,follower["starred_url"])
 ws.write(row,11,follower["subscriptions_url"])
 ws.write(row,12, follower["organizations_url"])
 ws.write(row,13,follower["repos_url"])
 ws.write(row,14,follower["events_url"])
 ws.write(row,15,follower["received_events_url"])
 ws.write(row,16,follower["type"])
 ws.write(row,17,follower["site_admin"])
 row += 1
w.save('followers.xls')