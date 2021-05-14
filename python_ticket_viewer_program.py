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

#the next block of code is to try and GET request a list of all the tickets in my account
import requests

# Set the request parameters
url = 'https://musubimez.zendesk.com/api/v2/groups.json'
user = 'marianne.lynch@gmail.com'
pwd = 'F3D3XR1s1ng'

# Do the HTTP get request
response = requests.get(url, auth=(user, pwd))

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()

# Example 1: Print the name of the first group in the list
print( 'First group = ', data['groups'][0]['name'] )

# Example 2: Print the name of each group in the list
group_list = data['groups']
for group in group_list:
    print(group['name'])
