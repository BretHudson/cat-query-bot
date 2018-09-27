import requests
import twitter
from local_settings import *

def generate_google_search_params(api_key, cx_id, q, safe):
	params = { 'key': api_key, 'cx': cx_id, 'q': q, 'searchType': "image", 'safe': safe };
	return params

def get_image_links_from_json(json):
	try:
		items = json['items']
		image_links = []
		for i in range(len(items)):
			image = items[i]['link']
			image_links.append(image)
		return image_links
	except KeyError:
		return []

# Borrowed from Tom Meagher's heroku_ebooks (https://github.com/tommeagher/heroku_ebooks)
def connect():
	return twitter.Api(consumer_key=MY_CONSUMER_KEY,
                       consumer_secret=MY_CONSUMER_SECRET,
                       access_token_key=MY_ACCESS_TOKEN_KEY,
                       access_token_secret=MY_ACCESS_TOKEN_SECRET,
                       tweet_mode='extended')

def post_tweets(word, images, total_results):
	api = connect()
	query_str = "\"" + word + " cat\" found "
	results_str = "  (total wesults: " + total_results + ")"
	success_text = "and pet sum cats ^.^"
	fail_text = "no cats v.v"
	str = query_str + (success_text if total_results != "0" else fail_text) + results_str
	if Debug:
		print("\nTweet text would be: ", str)
	else:
		status = api.PostUpdate(str, media=images[:4])
		print('\n', status)

if __name__ == "__main__":
	# Get variables from local_settings
	api_key = GOOGLE_API_KEY
	cx_id = GOOGLE_CUSTOM_SEARCH_ID
	safe = "active" if SAFE_SEARCH else "off"
	
	# Get latest word
	with open('mywords.txt', 'r') as fin:
	    data = fin.read().splitlines(True)
	
	try:
		word = data[0].rstrip()
		params = generate_google_search_params(api_key, cx_id, "\"" + word + "\" \"cat\"", safe)
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
			
			post_tweets(word, image_links, total_results)
			
			# Remove the word from our text file
			with open('testwords.txt', 'w') as fout:
			    fout.writelines(data[1:])
		
		print('\nSuccessfully finished\n')
	except IndexError:
		print('\nFailed: Words list is empty\n')