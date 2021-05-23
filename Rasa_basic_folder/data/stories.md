
## interactive_story_1
* goodbye
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* goodbye

## interactive_story_3
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_4
* greet
    - utter_greet
* goodbye
    - action_restart

## interactive_story_5
* greet
    - utter_greet
* dissmiss
    - utter_goodbye
    - action_restart
	
## interactive_story_6
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_location
	- slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_goodbye
    - export

## interactive_story_7
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_location
	- slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* affirm
    - utter_goodbye
    - export

## interactive_story_8
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_location
	- slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_goodbye

## interactive_story_9
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- action_check_location
	- slot{"check_resp": true}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* goodbye
    - utter_goodbye

## interactive_story_10
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - export


## interactive_story_11
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
	- action_check_location
	- slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* stop

## interactive_story_12
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
	- action_check_location
	- slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "mumbai"}

## interactive_story_13
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye
    
    
## interactive_story_14
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye


## interactive_story_15
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye

## interactive_story_16
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
	- action_check_location
    - utter_ask_cuisine
* location{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "bengaluru"}
	- slot{"emailbody": "Showing you top rated restaurants:\nYauatcha in Raheja Towers, Bandra Kurla Complex, Mumbai has been rated 4.7\n And the average price for two people is: 2800\nPa Pa Ya in Level 3, Palladium Mall, Senapati Bapat Marg, Lower Parel, Mumbai has been rated 4.6\n And the average price for two people is: 2000\nPa Pa Ya in G-2, Ground Floor, Third, North Avenue, Maker Maxity, Bandra Kurla Complex, Mumbai has been rated 4.6\n And the average price for two people is: 2000\nHakkasan in 206, Krystal, Waterfield Road, Linking Road, Bandra West has been rated 4.5\n And the average price for two people is: 2600\nMamagoto in 133, Ground Floor, Gazebo House, Hill Road, Bandra West, Mumbai, Maharashtra has been rated 4.5\n And the average price for two people is: 1500\nPa Pa Ya in Hotel Diplomat, Whitehouse Building, 24 - 26, B.K Boman Behram Marg, Apollo Bunder, Colaba, Mumbai has been rated 4.5\n And the average price for two people is: 2000\nJia The Oriental Kitchen in 2, Dhanraj Mahal, C. S. Marg, Colaba, Mumbai has been rated 4.5\n And the average price for two people is: 2500\nShaollin Temple in Krishna Avtar Building, Plot F/3, Palm Beach Road, Sector 14, CBD-Belapur, Navi Mumbai has been rated 4.4\n And the average price for two people is: 1000\nChina Bistro in Ground Floor, Infinity Shopping Complex, Vasant Vihar, Thane West has been rated 4.4\n And the average price for two people is: 1500\nThe Fatty Bao in Shop 1, Ground Floor, Sentinel Building, Hiranandani Business Park, Powai, Mumbai has been rated 4.3\n And the average price for two people is: 1800\n"}
    - utter_request_email
	- slot{"email": "vedulaaishwarya@gmail.com"}
	- action_send_email
* dissmiss
    - utter_goodbye
    - action_restart

## interactive_story_17
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"got_all": "yes"}
* affirm
    - utter_request_email
	- action_send_email
* email{"email": "siddakka_upgrad@gmail.com"}
    - slot{"email": "siddakka_upgrad@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_18
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"got_all": "yes"}
    - utter_email_prompt
* dissmiss
    - utter_goodbye
    - action_restart
	
## interactive_story_19
* restaurant_search{"cuisine": "chinese", "location": "bengaluru"}
	- action_check_location
    - slot{"cuisine": "chinese"}
    - slot{"location": "bengaluru"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"got_all": "yes"}
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "siddakka_upgrad@gmail.com"}
    - slot{"email": "siddakka_upgrad@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart
	
## interactive_story_20
* greet
    - utter_greet
* restaurant_search{"price": "low", "location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - slot{"price": "low"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - action_send_email
    - utter_goodbye
    - action_restart
	
## interactive_story_21
* restaurant_search{"price": "low", "cuisine": "north indian", "location": "new delhi"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "new delhi"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_email_prompt
* dissmiss{"not": "no"}
    - utter_goodbye
    - action_restart

## interactive_story_22
* restaurant_search{"price": "low", "location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - slot{"price": "low"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "aishwarya_upgrad@gmail.com"}
    - slot{"email": "aishwarya_upgrad@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart
	
## interactive_story_23
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_email_prompt
* dissmiss
    - utter_goodbye
    - action_restart

## interactive_story_24
* restaurant_search{"cuisine": "italian", "location": "dharmavaram"}
    - slot{"cuisine": "italian"}
    - slot{"location": "dharmavaram"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_25
* restaurant_search{"price": "low", "cuisine": "italian", "location": "Delhi"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Delhi"}
    - slot{"price": "low"}
    - action_search_restaurants
* goodbye
    - utter_email_prompt
* email{"email": "aishwarya_upgrad@protonmail.com"}
    - slot{"email": "aishwarya_upgrad@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart
	
## interactive_story_26
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
* goodbye
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "siddakka_upgrad@gmail.com"}
    - slot{"email": "siddakka_upgrad@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart
	
## interactive_story_27
* restaurant_search{"price": "low", "cuisine": "italian", "location": "Delhi"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Delhi"}
    - slot{"price": "low"}
    - action_search_restaurants
* goodbye
    - utter_email_prompt
* email{"email": "siddakka_upgrad@gmail.com"}
    - slot{"email": "siddakka_upgrad@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_28
* restaurant_search{"price": "high", "location": "Delhi"}
    - slot{"location": "Delhi"}
    - slot{"price": "high"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - utter_email_prompt
* dissmiss
    - utter_goodbye
    - action_restart
	
## interactive_story_29
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "bengaluru"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bengaluru"}
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
* restaurant_search
    - utter_request_email
* email{"email": "aishwarya_upgrad@iiitb.net"}
    - slot{"email": "aishwarya_upgrad@iiitb.net"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_30
* restaurant_search{"price": "high", "location": "dharmavaram"}
    - slot{"location": "dharmavaram"}
    - slot{"price": "high"}
    - utter_ask_cuisine
* cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_31
* restaurant_search{"price": "low", "cuisine": "italian", "location": "bengaluru"}
    - slot{"cuisine": "italian"}
    - slot{"location": "bengaluru"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_email_prompt
* dissmiss
    - utter_goodbye
    - action_restart

## interactive_story_32
* greet
    - utter_greet
* restaurant_search
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}
    - utter_ask_location
* location{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "foodie@hotmail.com"}
    - slot{"email": "foodie@hotmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart
	
## interactive_story_33
* greet
    - utter_greet
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
* dissmiss

## interactive_story_34
* restaurant_search{"price": "high", "cuisine": "indian", "location": "jaipur"}
    - slot{"cuisine": "indian"}
    - slot{"location": "jaipur"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* dissmiss
    - utter_goodbye
    - action_restart
	
## interactive_story_35
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}
    - utter_ask_location
* location{"location": "jalandhar"}
    - slot{"location": "jalandhar"}
    - action_search_restaurants
    - utter_email_prompt
* email{"email": "siddakka_upgrad@gmail.com"}
    - slot{"email": "siddakka_upgrad@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_36
* restaurant_search{"cuisine": "italian", "location": "dharmavaram"}
    - slot{"cuisine": "italian"}
    - slot{"location": "dharmavaram"}
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - reset_slots
    - utter_email_prompt
* email{"email": "aishwarya_upgrad@gmail.com"}
    - slot{"email": "aishwarya_upgrad@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_37
* restaurant_search{"price": "high", "cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - slot{"price": "high"}
    - utter_ask_location
* location{"location": "jodhpur"}
    - slot{"location": "jodhpur"}
    - action_search_restaurants
    - slot{"location": "jodhpur"}
    - slot{"price": "high"}
    - slot{"cuisine": "italian"}
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "aishwarya_upgrad@gmail.com"}
    - slot{"email": "aishwarya_upgrad@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_38
* restaurant_search{"cuisine": "italian", "location": "bengaluru"}
    - slot{"cuisine": "italian"}
    - slot{"location": "bengaluru"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "siddakka_upgrad@gmail.com"}
    - slot{"email": "siddakka_upgrad@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_39
* restaurant_search{"cuisine": "italian", "location": "dharmavram"}
    - slot{"cuisine": "italian"}
    - slot{"location": "dharmavram"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location_valid": "not"}

## interactive_story_40
* restaurant_search{"cuisine": "italian", "location": "dharmavram"}
    - slot{"cuisine": "italian"}
    - slot{"location": "dharmavram"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location_valid": "not"}

## interactive_story_41
* restaurant_search{"cuisine": "italian", "location": "dharmavaram"}
    - slot{"cuisine": "italian"}
    - slot{"location": "dharmavaram"}
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_42
* greet
    - utter_greet
* restaurant_search{"price": "low", "location": "anantapur"}
    - slot{"location": "anantapur"}
    - slot{"price": "low"}
    - utter_ask_cuisine
* cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_43
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - utter_ask_cuisine
* cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* dissmiss
    - utter_goodbye
    - action_restart

## interactive_story_44
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "siddakka_upgrad@gmail.com"}
    - slot{"email": "siddakka_upgrad@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_45
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - utter_ask_location
* location{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_search_restaurants
    - utter_email_prompt
* email{"email": "aishwarya_upgrad@gmail.com"}
    - slot{"email": "aishwarya_upgrad@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_46
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}
    - utter_ask_location
* location{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_search_restaurants
    - utter_email_prompt
* dissmiss
    - action_restart

## interactive_story_48
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - utter_ask_location
* location{"location": "dharmavaram"}
    - slot{"location": "dharmavaram"}
    - action_search_restaurants
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_49
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_location
* location{"location": "culcutta"}
    - slot{"location": "culcutta"}
    - utter_ask_cuisine
* cuisine{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_50
* greet
    - utter_greet
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}

## interactive_story_51
* greet
    - utter_greet
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_location
* location{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - utter_ask_cuisine
* location{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_search_restaurants
    - utter_email_prompt
* dissmiss{"not": "never"}
    - utter_goodbye
    - action_restart

## interactive_story_52
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_location
* location{"location": "jodhpur"}
    - slot{"location": "jodhpur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "aishwarya_upgrad@gmail.com"}
    - slot{"email": "aishwarya_upgrad@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_53
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - utter_ask_location
* location{"location": "varanasi"}
    - slot{"location": "varanasi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - utter_email_prompt
* dissmiss
    - utter_goodbye
    - action_restart

## interactive_story_54
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_location
* location{"location": "jhansi"}
    - slot{"location": "jhansi"}
    - utter_ask_cuisine
* cuisine{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_email_prompt
* dissmiss
    - utter_goodbye
    - action_restart

## interactive_story_55
* greet
    - utter_greet
* restaurant_search{"price": "low", "cuisine": "mexican", "location": "jodhpur"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "jodhpur"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_email_prompt
* dissmiss
    - utter_goodbye
    - action_restart

## interactive_story_56
* greet
    - utter_greet
* restaurant_search{"price": "high", "cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "aishwarya_upgrad@gmail.com"}
    - slot{"email": "aishwarya_upgrad@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart
	
## interactive_story_57
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Yanam"}
    - slot{"location": "Yanam"}
	- action_check_location
	- slot{"check_resp": false}
    - utter_we_dont_operate
    - utter_goodbye
    - export

## interactive_story_58
* greet
    - utter_greet
* restaurant_search{"location": "Yanam"}
    - slot{"location": "Yanam"}
	- action_check_location
	- slot{"check_resp": false}
	- utter_we_dont_operate
    - utter_goodbye
    - export
	
## interactive_story_59
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
	- action_check_location
    - utter_ask_cuisine
* location{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "bengaluru"}
	- slot{"emailbody": "Showing you top rated restaurants:\nYauatcha in Raheja Towers, Bandra Kurla Complex, Mumbai has been rated 4.7\n And the average price for two people is: 2800\nPa Pa Ya in Level 3, Palladium Mall, Senapati Bapat Marg, Lower Parel, Mumbai has been rated 4.6\n And the average price for two people is: 2000\nPa Pa Ya in G-2, Ground Floor, Third, North Avenue, Maker Maxity, Bandra Kurla Complex, Mumbai has been rated 4.6\n And the average price for two people is: 2000\nHakkasan in 206, Krystal, Waterfield Road, Linking Road, Bandra West has been rated 4.5\n And the average price for two people is: 2600\nMamagoto in 133, Ground Floor, Gazebo House, Hill Road, Bandra West, Mumbai, Maharashtra has been rated 4.5\n And the average price for two people is: 1500\nPa Pa Ya in Hotel Diplomat, Whitehouse Building, 24 - 26, B.K Boman Behram Marg, Apollo Bunder, Colaba, Mumbai has been rated 4.5\n And the average price for two people is: 2000\nJia The Oriental Kitchen in 2, Dhanraj Mahal, C. S. Marg, Colaba, Mumbai has been rated 4.5\n And the average price for two people is: 2500\nShaollin Temple in Krishna Avtar Building, Plot F/3, Palm Beach Road, Sector 14, CBD-Belapur, Navi Mumbai has been rated 4.4\n And the average price for two people is: 1000\nChina Bistro in Ground Floor, Infinity Shopping Complex, Vasant Vihar, Thane West has been rated 4.4\n And the average price for two people is: 1500\nThe Fatty Bao in Shop 1, Ground Floor, Sentinel Building, Hiranandani Business Park, Powai, Mumbai has been rated 4.3\n And the average price for two people is: 1800\n"}
    - utter_request_email
	- slot{"email": "vedulaaishwarya@gmail.com"}
	- action_send_email
* dissmiss
    - utter_goodbye
    - action_restart