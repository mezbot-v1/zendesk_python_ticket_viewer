#this script will request and display all the tickets for my zendesk account

#hopefully it will paginate through them too ^_^'
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

# Exercise 3: The elif statement
userReply = input("Welcome to the Zendesk Ticket Viewer! Would you like to print all the tickets or a single ticket? (Type all or single) ")

if userReply == "all":
    # All the tickets
    url = zendesk + '/api/v2/tickets'


    response = session.get(url, auth=(credentials))
    #print(response) below is to verify that it works - currently commented out 
    #print (response.json())

    if response.status_code != 200:
        print('Argh! Something went wrong. Technically speaking, we have an error with status code {}'.format(response.status_code))

    #as part of my initial testing I wanted to verify that it was printing the total amount of tickets but as this is not required for the final assessment it is now commented out
    # data = response.json()
    # total_tickets = data['count']
    # print ('\n')
    # print ('Total Tickets:', total_tickets)
    # print ('\n' '\n')

    #paginate through the results so that 25 max are displayed at any given time

    url = zendesk + '/api/v2/tickets.json?page[size]=25'

    while url:
        response = session.get(url, auth=(credentials))
        data = response.json()
        ticket_list = data['tickets']
        for ticket in ticket_list:
            print("Ticket ID:", ticket['id']) 
            print("Created at:",  ticket['created_at']) 
            print("Updated at:", ticket['updated_at'])
            print("Subject: ",ticket['subject']) 
            print ("Description: ", ticket['description']) 
            print("Status: ",ticket['status'])
            print("Requester ID: ", ticket['requester_id']) 
            print("Assignee ID:", ticket['assignee_id'])
            print('\n')

        #for ticket in data['tickets']:
        # print(ticket['id'])

        if data['meta']['has_more']:
            url = data['links']['next']
        else:
            url = None
elif userReply == "single":
    single = int(input("What ticket number would you like? (Type a number between 203-262) "))
    
    # test if input is between 203-262
    if 203 <= single <= 262:
        url = zendesk + '/api/v2/tickets/' + str(single) + '.json'
        #print(url)
        response = session.get(url, auth=(credentials))
        data = response.json()
        print("Ticket ID:", data['ticket']['id']) 
        print("Created at:",  data['ticket']['created_at']) 
        print("Updated at:", data['ticket']['updated_at'])
        print("Subject: ",data['ticket']['subject']) 
        print ("Description: ", data['ticket']['description']) 
        print("Status: ",data['ticket']['status'])
        print("Requester ID: ", data['ticket']['requester_id']) 
        print("Assignee ID:", data['ticket']['assignee_id'])
        print('\n')
    else: 
        print("D'oh! Your number was not between the desired range. Exiting. Try running the program again.")

else:
    print("Ruh roh. Your input didn't match the request. Exiting. Try running the program again.")
