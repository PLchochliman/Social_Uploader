import requests
import facebook as fb
import os
from dotenv import load_dotenv

load_dotenv()

authorisation = {
    "page_id"      :  os.getenv("FB_Page_id"),
    "access_token" : os.getenv("FB_Access_token")
    }


def FB_uploader(text, filepath):
    try:
        graph = fb.GraphAPI(authorisation['access_token'])
        #resp = graph.get_object('me/accounts')
        #page_access_token = None
        #for page in resp['data']:
        #    if page['id'] == authorisation['page_id']:
        #        page_access_token = page['access_token']
        #page_opened = fb.GraphAPI(page_access_token)



        graph.put_photo(image=open(filepath,"rb"), message=text)
    except Exception as e:
        print(f"An error occurred: {e}")
        print("FB Posting Failed!")

#page_opened.put_object("me", "feed", image=open(filepath,"rb"), message=text)

