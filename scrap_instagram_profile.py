# used to download the page from istagram by get request
import requests
# used to parse the server response to html to select specific atteributes and tages
from bs4 import BeautifulSoup
# used to deal with json in python and convert a json (string) to a dictionnary
import json
# used to deal with scv files easelly
import csv

username = input('Enter the username : \n')

while username == '':
	print('Enter the username please !')
	username = input('Enter your username')

# web page url
url = "https://www.instagram.com/{}/".format(username)
#make e GET request to download the page
try:
	response = requests.get(url)
except Exception as e:
	raise e

# Ensure that the username exists and the response is OK
if not response.ok:
	print('response not found, the username is correct ?')
	raise requests.exceptions.RequestException

# parse the text response to html
soup = BeautifulSoup(response.text, features='html.parser')

# select the content of 4 fourthy script that contain data
string = soup.find_all('script')[4].string

# remove useless data
string = string.replace(';', '').replace('window._sharedData = ', '')

#convert the string to a dictionnary
data = json.loads(string)

#select the user info
user = data['entry_data']['ProfilePage'][0]['graphql']['user']

# extract the nombre of fllowers
fllowers = user['edge_followed_by']['count']

# extract the nombre of fllowing
fllowing = user['edge_follow']['count']

name = user['full_name']

username = user['username']

image = user['profile_pic_url']

posts = user['edge_owner_to_timeline_media']['edges']

# open a csv file in append mode to add user data.
with open('data.csv', 'a', newline='\n') as csvfile : 
	csv_file = csv.writer(csvfile)
	csv_file.writerow(['username', 'name','image', 'fllowers', 'fllowing', 'posts'])
	csv_file.writerow([username, name,image, fllowers, fllowing, len(posts)])
	print('the process successed !')
