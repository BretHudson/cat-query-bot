import requests
from local_settings import *

def generate_google_search_params(api_key, cx_id, q, safe):
	params = { 'key': api_key, 'cx': cx_id, 'q': q, 'searchType': "image", 'safe': safe };
	return params

def get_image_links_from_json(json):
	items = json['items']
	image_links = []
	for i in range(len(items)):
		image = items[i]['image']
		image_links.append(image['contextLink'])
	return image_links

if __name__ == "__main__":
	# Get variables from local_settings
	api_key = GOOGLE_API_KEY
	cx_id = GOOGLE_CUSTOM_SEARCH_ID
	safe = "active" if SAFE_SEARCH else "off"
	
	# Retrieve JSON data containing images
	params = generate_google_search_params(api_key, cx_id, "sniper cat", safe)
	if TEST_SCRAPE_URL:
		r = requests.get(TEST_SCRAPE_URL)
	else:
		r = requests.get("https://www.googleapis.com/customsearch/v1", params=params)
	print("Requesting data from", r.url)
	
	print(r) # Prints response code
	if r.status_code == requests.codes.ok:
		json = r.json()
		
		# Get total result count
		total_results = json['queries']['request'][0]['totalResults']
		
		# Get images
		image_links = get_image_links_from_json(json)
		print('\nFound images', image_links)
	
	print('\nSuccessfully finished\n')