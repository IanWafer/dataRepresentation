import requests
import json
#from xlwt import *

#url = "https://reports.sem-o.com/api/v1/documents/static-reports"
url = "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View&Date=>2020-11-01"
response  = requests.get(url)
data  = response.json()

listOfReports = []
#output to console
#print(data)

for item in data["items"]:
    print(item["ResourceName"])
    listOfReports.append(item["ResourceName"])

for ReportName in listOfReports:
    #print(ReportName)
    url = "https://reports.sem-o.com/api/v1/documents/"+ReportName
    print(url)
    repsonse = requests.get(url)
    aReport= response.json()
    for row in aReport["rows"]:
        print(row["ImbalancePrice"])

#other code
# sace this to a file
filename = 'allreports.json'
# Writing JSON data
f = open(filename, 'w')
json.dump(data, f, indent=4)
