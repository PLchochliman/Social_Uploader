import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()


short_lived_user_access_token = os.getenv("FB_Access_token")
app_secret = os.getenv("FB_App_secret")
page_id = os.getenv("FB_Page_id")
app_id = os.getenv("FB_App_id")

response = requests.get(f"https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id={app_id}&client_secret={app_secret}&fb_exchange_token={short_lived_user_access_token}")
user_access_token = json.loads(response.text)
user_access_token = user_access_token['access_token']

response = requests.get(f"https://graph.facebook.com/{page_id}?fields=access_token&access_token={user_access_token}")
user_access_token = json.loads(response.text)
user_access_token = user_access_token['access_token']

print(f"Your live living user token is: {user_access_token}")
