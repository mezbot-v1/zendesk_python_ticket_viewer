#this template is for messing around with python hitting the zendesk api and returning a filtered query listing certain fields
#install requests library for HTTP requests 
#pip3 install requests

#request to connect to zendesk api
#import requests library for simple access to HTTP and set request parameters
import requests
from requests.models import Response
import json
import os
from dotenv import load_dotenv

load_dotenv()

credentials = (os.getenv('ZENDESK_EMAIL'), os.getenv('ZENDESK_PASSWORD'))
session = requests.Session()
session.auth = credentials
zendesk = os.getenv('ZENDESK_URL')

#data = Response.json()
#data = { "ticket": { "url": ''  "id": } { "updated_at": '' ;{ "subject": '' } { "description":'' } {"priority" } { "status": "requester_id" } { "assignee_id" } }

#API endpoint for 'incremental ticket exporter' to list all tix (??)
url = zendesk + '/api/v2/incremental/tickets/cursor.json?start_time=1620452025'

response = session.get(url, auth=(credentials))
#print(response) below is to verify that it works - currently commented out 
print(response)

if response.status_code != 200:
    print('Argh! Something went wrong. Technically speaking, we have an error with status code {}'.format(response.status_code))


#tickets_list = data['tickets']
#for tickets in tickets_list :
#    print(tickets[url])

