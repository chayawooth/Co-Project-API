import requests
import json
import sys
import datetime
from configure import *
try:
    ticketid=sys.argv[1]
    times=datetime.datetime.now() - datetime.timedelta(seconds=3)
    nows = datetime.datetime.now()
    reportdate=times.strftime("%Y-%m-%dT%H:%M:%S")
    affecteddate=times.strftime("%Y-%m-%dT%H:%M:%S")

    url = "http://10.50.90.202:8080/nttservice/msom-activity"
    headers = {'Content-type': 'application/json'}
    payload = json.dumps({ "ticketid" : ticketid ,
                                       "externalsystem" : "CFM" ,
                                       "ciname" : "CCS0001A" ,
                                       "subject" : "Test subject" ,
                                       "assignedactivityowner" : "UPC01E-RF"
                           } )
    print("Now time : ", nows)
    print("New time : ", times)
    print(payload)
    response = requests.request("post", url, headers=headers, data=payload,auth = ( user , pwd ))
    print(requests.get(url).headers)
    #print(response.headers)
    print(response.text)
except:
    print("please input ticketid ")

print("Process Done!!")