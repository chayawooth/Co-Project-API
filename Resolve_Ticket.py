import requests
import json
import sys
import datetime
from configure import *
try:
    ticketid=sys.argv[1]
    cause=sys.argv[2]
    subcause=sys.argv[3]
    times=datetime.datetime.now() - datetime.timedelta(seconds=3)
    nows = datetime.datetime.now()
    reportdate=times.strftime("%Y-%m-%dT%H:%M:%S")
    affecteddate=times.strftime("%Y-%m-%dT%H:%M:%S")

    url = "http://10.50.90.202:8080/nttservice/msom-ticket"
    headers = {'Content-type': 'application/json'}
    payload = json.dumps({ "ticketid" : ticketid ,
                                        "status" : "RESOLVED" ,
                                        "externalsystem" : "CFM" ,
                                        "updatedby" : "01028197" ,
                                        "failurecode" : "MSOM" ,
                                        "problemcode" : cause ,
                                        "causecode" : subcause ,
                                        "remedycode" : "MS01" ,
                                        "restorationdate" : reportdate
                                        } )
    print("Now time : ", nows)
    print("New time : ", times)
    print(payload)
    response = requests.request("patch", url, headers=headers, data=payload,auth = ( user , pwd ))
    print(requests.get(url).headers)
    #print(response.headers)
    print(response.text)
except:
    print("please input ticketid  cause subcause ")

print("Process Done!!")