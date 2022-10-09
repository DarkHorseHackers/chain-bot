import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://api.imgflip.com/caption_image"

imgflip_username = os.getenv('IMGFLIP_USERNAME')
imgflip_password = os.getenv('IMGFLIP_PASSWORD')

payload = 'template_id=130331290&username=' + imgflip_username + '&password=' + imgflip_password + '&text0=i%20bet%20he\'s%20thinking%20about%20other%20women'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

def generate_meme(text: str):
    try:
        data = payload + '&text1=' + text
        response = requests.request("POST", url, headers=headers, data=data)
        response_json = json.loads(response.text)
        img_url = response_json["data"]["url"]

        print(img_url)

        img_data = requests.get(img_url).content
        with open('meme.jpg', 'wb') as handler:
            handler.write(img_data)
    except Exception as e:
        print("Error: ", e)