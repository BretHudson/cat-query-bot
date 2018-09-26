import requests
from local_settings import *

def generate_google_search_params(api_key, cx_id, q, safe):
	params = { 'key': api_key, 'cx': cx_id, 'q': q, 'searchType': "image", 'safe': safe };
	return params

if __name__ == "__main__":
	# Get variables from local_settings
	api_key = GOOGLE_API_KEY
	cx_id = GOOGLE_CUSTOM_SEARCH_ID
	safe = "active" if SAFE_SEARCH else "off"
	
	# Retrieve JSON data containing images
	params = generate_google_search_params(api_key, cx_id, "sniper cat", safe)
	r = requests.get("https://www.googleapis.com/customsearch/v1", params=params)
	print("Requesting data from", r.url)
	
	print(r) # Prints response code
	if r.status_code == requests.codes.ok:
		#print(r.text)
		json = r.json
		print(r.json)