import requests
import json
import sys
import datetime
from configure import *

try:
    ticketid=sys.argv[1]
    worklog=sys.argv[2]
    times=datetime.datetime.now() - datetime.timedelta(hours=12)
    nows = datetime.datetime.now()
    reportdate=times.strftime("%Y-%m-%dT%H:%M:%S")
    affecteddate=times.strftime("%Y-%m-%dT%H:%M:%S")
    url = "http://10.50.90.202:8080/nttservice/msom-ticket-worklog"
    headers = {'Content-type': 'application/json'}
    payload = json.dumps({ "createby" : "01028197" ,
                            "recordkey" : ticketid ,
                            "subject" : "Update log" + ticketid ,
                            "longdescription" : worklog,
                            "senttocfm" :  "1"
                           } )
    print("Now time : ", nows)
    print("New time : ", times)
    print(payload)
    response = requests.request("post", url, headers=headers, data=payload,auth = ( user , pwd ))
    print(requests.get(url).headers)
    #print(response.headers)
    print(response.text)
except:
    print("please input ticketid  Worklog ")

print("Process Done!!")