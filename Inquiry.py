import requests
import sys


url ="http://10.50.90.202:8080/nttservice/msom-ticket?"
try:
    tt=sys.argv[1]
    ticketid = "ticketid=" + tt
    print(ticketid)
    response = requests.get(url + ticketid)

    #Result
    print(response.json()['msomticketlist'][0])

    print("####### TT Inquiry ######")
    print("ticketid : ", response.json()['msomticketlist'][0]['ticketid'])
    print("tickettype : ",response.json()['msomticketlist'][0]['tickettype'])
    print("status : ",response.json()['msomticketlist'][0]['status'])
    print("subject : ",response.json()['msomticketlist'][0]['subject'])
    print("longdescription : ",response.json()['msomticketlist'][0]['longdescription'])
    print("classification : ",response.json()['msomticketlist'][0]['classification'])
    print("severity : ",response.json()['msomticketlist'][0]['severity'])
    print("urgency : ",response.json()['msomticketlist'][0]['urgency'])
    print("slaresolutiontime : ",response.json()['msomticketlist'][0]['slaresolutiontime'])
    print("owner : ",response.json()['msomticketlist'][0]['owner'])
    print("ownergroup : ",response.json()['msomticketlist'][0]['ownergroup'])
    print("createdby : ",response.json()['msomticketlist'][0]['createdby'])
    print("createdbyname : ",response.json()['msomticketlist'][0]['createdbyname'])
    print("reportedby : ",response.json()['msomticketlist'][0]['reportedby'])
    print("reportedbyname : ",response.json()['msomticketlist'][0]['reportedbyname'])
    print("externalsystem : ",response.json()['msomticketlist'][0]['externalsystem'])
    print("externalsystemuser : ",response.json()['msomticketlist'][0]['externalsystemuser'])
    print("reportdate : ",response.json()['msomticketlist'][0]['reportdate'])
    print("affecteddate : ",response.json()['msomticketlist'][0]['affecteddate'])
    print("creationdate : ",response.json()['msomticketlist'][0]['creationdate'])
    print("restorationdate : ",response.json()['msomticketlist'][0]['restorationdate'])
    print("externalsystemuser : ",response.json()['msomticketlist'][0]['externalsystemuser'])
    print("########### End ############")
except:
    print("pls input tt")


print("test commit by chayawooth")