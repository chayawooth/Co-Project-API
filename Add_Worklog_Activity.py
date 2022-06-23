import requests
import json
import sys
import datetime
from configure import *
try:
    wonumber=sys.argv[1]
    subject = sys.argv[2]
    longdescription = sys.argv[3]
    times=datetime.datetime.now() - datetime.timedelta(hours=12)
    nows = datetime.datetime.now()
    reportdate=times.strftime("%Y-%m-%dT%H:%M:%S")
    affecteddate=times.strftime("%Y-%m-%dT%H:%M:%S")

    url = "http://10.50.90.202:8080/nttservice/msom-activity-worklog"
    headers = {'Content-type': 'application/json'}
    payload = json.dumps({ "createby": "01028197",
                                        "recordkey": wonumber,
                                        "subject": "Auto Bot MSOM",
                                        "longdescription": longdescription,
                                        "senttocfm": "1",


                           } )
    print("Now time : ", nows)
    print("New time : ", times)
    print(payload)
    response = requests.request("post", url, headers=headers, data=payload,auth = ( user , pwd ))
    print(requests.get(url).headers)
    #print(response.headers)
    print(response.text)
except:
    print("please input wonumber  subject longdescription")

print("Process Done!!")