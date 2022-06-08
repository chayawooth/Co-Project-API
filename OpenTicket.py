import requests
import json
import sys
import datetime

try:
    subject=sys.argv[1]
    longdescription = sys.argv[2]
    times=datetime.datetime.now() - datetime.timedelta(seconds=3)
    nows = datetime.datetime.now()
    reportdate=times.strftime("%Y-%m-%dT%H:%M:%S")
    affecteddate=times.strftime("%Y-%m-%dT%H:%M:%S")

    url = "http://10.50.90.202:8080/nttservice/msom-ticket"
    headers = {'Content-type': 'application/json'}

    payload = json.dumps({
      "externalsystem": "CFM",
      "tickettype": "Incident",
      "subject": subject,
      "longdescription": longdescription,
      "classification" : "MSOM-CVIP-SQ \\ PROBLEM AREA \\ NEA",
      "createdby": "CFM",
      "reportedby": "01028197",
      "reportdate":  reportdate ,
      "affecteddate": affecteddate ,
    })
    print("Now time : ", nows)
    print("New time : ", times)
    print(payload)
    response = requests.request("POST", url, headers=headers, data=payload,auth = ("Chayawo" , "cdexswzaQ*01028197"))
    print(requests.get(url).headers)
    #print(response.headers)
    print(response.text)
except:
    print("please input subject longdescription")

print("Process Done!!")