#MEZ - YOU NEED TO RESOLVE THE CREDENTIALS ISSUE BEFORE GOING PUBLIC WITH THIS REPO
#install requests library for HTTP requests 
#pip3 install requests

#request to connect to zendesk api
import requests

credentials = 'marianne.lynch@gmail.com', 'F3D3XR1s1ng'
session = requests.Session()
session.auth = credentials
zendesk = 'https://musubimez.zendesk.com'

url = zendesk + '/api/v2/tickets.json?include=comment_count'
response = session.get(url)
#print(response) below is to verify that it works - currently commented out 
#print(response)

if response.status_code != 200:
    print('Argh! Something went wrong. Technically speaking, we have an error with status code {}'.format(response.status_code))
    exit()
#topic_posts = data['posts']

#note for mez - should you add that code check thingie in as a failsafe here?

#for post in topic_posts:
#    print(post['title'])
