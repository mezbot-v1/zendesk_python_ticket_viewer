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

#API endpoint for showing a single ticket on bash with specific ticket id (204)
#url = zendesk + '/api/v2/tickets/204.json'

# All the tickets
url = zendesk + '/api/v2/tickets'


response = session.get(url, auth=(credentials))
#print(response) below is to verify that it works - currently commented out 
#print (response.json())

if response.status_code != 200:
    print('Argh! Something went wrong. Technically speaking, we have an error with status code {}'.format(response.status_code))


data = response.json()
total_tickets = data['count']
print ('Total Tickets', total_tickets)

#Print each ticket in the list, selecting only the data we want to print (ie not the whole ticket)
ticket_list = data['tickets']
# for tickets in ticket_list:
#     print(tickets['id'], tickets['created_at'],tickets['updated_at'],tickets['subject'], tickets['description'], tickets['status'],tickets['requester_id'], tickets['assignee_id'])

for tickets in ticket_list:
     print("Ticket ID:", tickets['id']) 
     print("Created at:",  tickets['created_at']) 
     print("Updated at:", tickets['updated_at'])
     print("Subject: ",tickets['subject']) 
     print ("Description: ", tickets['description']) 
     print("Status: ",tickets['status'])
     print("Requester ID: ", tickets['requester_id']) 
     print("Assignee ID:", tickets['assignee_id'])
     print('\n')
