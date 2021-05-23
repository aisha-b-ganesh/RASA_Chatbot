from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

ZomatoData = pd.read_csv('zomato.csv')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']

def RestaurantSearch(City,Cuisine):
	TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))]
	return TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]

class ActionCheckLocation(Action):
    def name(self):
        return 'action_check_location'
        
    def run(self, dispatcher, tracker, domain):
        loc= tracker.get_slot('location')
        res = ValidateLocation(loc)
        return [SlotSet('check_resp',res)]
            
class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		#config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		results = RestaurantSearch(City=loc,Cuisine=cuisine)
		response=""
		if results.shape[0] == 0:
			response= "no results"
            #dispatcher.utter_message('Sorry we do not operate there yet! I can help you with another location')
		else:
			for restaurant in RestaurantSearch(loc,cuisine).iloc[:5].iterrows():
				restaurant = restaurant[1]
				response=response + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Address']} with avg cost {restaurant['Average Cost for two']} \n\n"
				
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]
		return [SlotSet('emailbody',response)]
        
        
        
class ActionSendMail(Action):
	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):
		receiver_address = tracker.get_slot('email')
		sender_address = 'frencha806@gmail.com'
		sender_pass  = 'Goal@2022'
		message = MIMEMultipart()
		message['From'] = sender_address
		message['TO'] = receiver_address
		message['Subject'] = 'Hello Foodie, here is your list of restaurants!'
		session = smtplib.SMTP('smtp.gmail.com',587)
		session.starttls()
		session.login(sender_address, sender_pass)
		body = tracker.get_slot('emailbody')
		message.attach(MIMEText(body,'plain'))
		text = message.as_string()
		server.sendmail(sender_address,receiver_address,text)
		server.quit()
		print('Mail Sent')
                
