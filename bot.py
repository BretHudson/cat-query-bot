import urllib.parse
from local_settings import *

def generate_google_search_url(api_key, cx_id, q, safe):
	params = { 'key': api_key, 'cx': cx_id, 'q': q, 'searchType': "image", 'safe': safe };
	return "https://www.googleapis.com/customsearch/v1?" + urllib.parse.urlencode(params)

if __name__ == "__main__":
	api_key = GOOGLE_API_KEY
	cx_id = GOOGLE_CUSTOM_SEARCH_ID
	safe = "active" if SAFE_SEARCH else "off"
	
	url = generate_google_search_url(api_key, cx_id, "sniper cat", safe)
	print(url)