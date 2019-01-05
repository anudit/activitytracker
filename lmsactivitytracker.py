import requests
from bs4 import BeautifulSoup
import os
import urllib
from getpass import getpass
from tqdm import tqdm
import csv
import time

print('loading...')
username = "an9316"
password = "#Bennett"
#username = input('Enter your bennett username: ')
#password = getpass('Enter your bennett password: ')

requestSession = requests.Session()
loginRequest = requestSession.post('http://lms.bennett.edu.in/login/index.php?authldap_skipntlmsso=1', data={'username': username, 'password': password, 'submit': ''})
loginHistory = loginRequest.history
loginHistoryLength = len(loginHistory)



if loginHistoryLength == 2:
	for i in range(0,2):
		names = {}
		with open('people.csv') as csv_file:
			reader = csv.reader(csv_file)
			names = dict(reader)
		r = requestSession.get('http://lms.bennett.edu.in/my/')
		
		soup = BeautifulSoup(r.content, 'html.parser')
		
		ul = soup.find_all("div", class_="user")
		#print(ul)
		
		for user in ul:
			userDat = user.find_all('a')[0]
			print(str(userDat.text).upper())        
			names.update({str(userDat.text).upper(): int(names.get(str(userDat.text).upper(),"0"))+1})
			
			
		with open('people.csv', 'w+') as csv_file:
			writer = csv.writer(csv_file)
			for key, value in names.items():
				writer.writerow([key, value])
		time.sleep(5)
		i=1
    
else:
    print('Invalild Login details ! Please close the window and re-run the program !')
	