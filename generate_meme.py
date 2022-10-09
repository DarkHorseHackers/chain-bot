import requests
import json
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

url = "https://api.imgflip.com/caption_image"

imgflip_username = os.getenv('IMGFLIP_USERNAME')
imgflip_password = os.getenv('IMGFLIP_PASSWORD')

payload = 'template_id=130331290&username=' + imgflip_username + '&password=' + imgflip_password
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

def generate_meme(text1: str, text0: str, replace_man_profile: bool = False, replace_woman_profile: bool = False):
    try:
        data = payload + '&text1=' + text1 + '&text0=' + text0
        response = requests.request("POST", url, headers=headers, data=data)
        response_json = json.loads(response.text)
        img_url = response_json["data"]["url"]

        print("meme url: ", img_url)

        img_data = requests.get(img_url).content
        with open('meme.jpg', 'wb') as handler:
            handler.write(img_data)    

        background = Image.open("meme.jpg")

        if replace_man_profile:
            man_profile = Image.open("man-profile.jpg")
            background.paste(man_profile, (650, 130), man_profile.convert('RGBA'))

        if replace_woman_profile:
            woman_profile = Image.open("woman-profile.jpg")
            background.paste(woman_profile, (230, 80), woman_profile.convert('RGBA'))

        background.save('meme.jpg')

    except Exception as e:
        print("Error: ", e)