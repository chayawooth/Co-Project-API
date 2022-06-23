import requests
import json
import sys
import datetime
from configure import *
try:
    wonumber=sys.argv[1]
    times=datetime.datetime.now() - datetime.timedelta(seconds=3)
    nows = datetime.datetime.now()
    reportdate=times.strftime("%Y-%m-%dT%H:%M:%S")
    affecteddate=times.strftime("%Y-%m-%dT%H:%M:%S")

    url = "http://10.50.90.202:8080/nttservice/msom-activity"
    headers = {'Content-type': 'application/json'}
    payload = json.dumps({ "wonum" : wonumber ,
                                        "externalsystem" : "CFM" ,
                                        "status" : "COMP" ,
                                        "updateby" : "01063472" ,
                                        "failurecode" : "MSOM" ,
                                        "problemcode" : "MS014" ,
                                        "causecode" : "MS0037" ,
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
    print("please input wonumber ")

print("Process Done!!")