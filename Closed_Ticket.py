import requests
import json
import sys
import datetime
from configure import *
try:
    ticketNum = sys.argv[1]
    cause = sys.argv[2]
    subcause = sys.argv[3]
    print("ticketNum :", ticketNum)
    print("cause :", cause)
    print("subcause :", subcause)
    times = datetime.datetime.now() - datetime.timedelta(hours=12)
    times=datetime.datetime.now() - datetime.timedelta(hours=12)
    nows = datetime.datetime.now()
    reportdate=times.strftime("%Y-%m-%dT%H:%M:%S")
    affecteddate=times.strftime("%Y-%m-%dT%H:%M:%S")
    url = "http://10.50.90.202:8080/nttservice/msom-ticket"
    headers = {'Content-type': 'application/json',"Content-Encoding": "gzip, deflate, br"}
    payload = json.dumps({
        "ticketid": ticketNum,
        "status": "RESOLVED",
        "externalsystem": "CFM",
        "updatedby": "01028197",
        "failurecode": "MSOM",
        "problemcode": cause,
        "causecode": subcause,
        "remedycode": "MS01",
        "restorationdate": reportdate })
    print(payload)
    response = requests.request("PATCH", url, headers=headers, data=payload, auth=(user , pwd))
    print(requests.get(url).headers)
    # print(response.headers)
    print(response.text)
except:
    print("please ticketNum  cause subcause ")
    print("TcticketNum MS014 MS0037")

print("Closed Done!!")
