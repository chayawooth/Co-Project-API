import requests
import json
import sys
import datetime

try:
    ticketNum=sys.argv[1]
    times=datetime.datetime.now() - datetime.timedelta(seconds=3)
    nows = datetime.datetime.now()
    reportdate=times.strftime("%Y-%m-%dT%H:%M:%S")
    affecteddate=times.strftime("%Y-%m-%dT%H:%M:%S")

    url = "http://10.50.90.202:8080/nttservice/msom-ticket"
    headers = { 'Content-type' : 'application/json' , "Content-Encoding" : "gzip, deflate, br" }

    payload = json.dumps({
        "wonum": "A4660701",
        "externalsystem": "CFM",
        "status": "COMP",
        "updateby": "01028197",
        "failurecode": "MSOM",
        "problemcode": "MS014",
        "causecode": "MS0037",
        "remedycode": "MS01",
        "restorationdate": nows
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