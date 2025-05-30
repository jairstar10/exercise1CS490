import requests
import json

url = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info"

data = {
    "UCID": "eja33",  
    "first_name": "Eidan",
    "last_name": "Arriaga",
    "github_username": "jairstar10",
    "discord_username": "jairstar10",
    "favorite_cartoon": "Regular Show",
    "favorite_language": "Python",
    "movie_or_game_or_book": "Rush Hour"
}

headers = {
    "Content-Type": "application/json"
}

try:
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
