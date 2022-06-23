import requests
import json
import sys
import datetime
from configure import *
try:
    ticketid=sys.argv[1]
    assignedactivityowner=sys.argv[2]
    times=datetime.datetime.now() - datetime.timedelta(hours=12)
    nows = datetime.datetime.now()
    reportdate=times.strftime("%Y-%m-%dT%H:%M:%S")
    affecteddate=times.strftime("%Y-%m-%dT%H:%M:%S")

    url = "http://10.50.90.202:8080/nttservice/msom-activity"
    headers = {'Content-type': 'application/json'}
    payload = json.dumps({ "ticketid" : ticketid ,
                                       "externalsystem" : "CFM" ,
                                       "ciname" : "" ,
                                       "subject" : "Test subject" ,
                                       "assignedactivityowner" : "MSOMSC32"
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
    print("Ex. TT12345678990 MSOMSC32")

print("Process Done!!")