import dotenv
import os
import requests
import json

dotenv.load_dotenv()

cooldowns = {
    "movement": 0
}

# check if movement is on cooldown
# check if i can move that way
# create graph of known rooms

def move(direction):
    if cooldowns["movement"] > 0:
        print("err: movement on cooldown")
        return

    # "Content-Type: application/json" -d '{"direction":"n"}
    headers = {
        "Authorization": f"Token {os.environ['API_KEY']}",
        "Content-Type": "application/json",
    }

    payload = { "direction": direction }

    response = requests.post("https://lambda-treasure-hunt.herokuapp.com/api/adv/move/", 
        data=json.dumps(payload), headers=headers)

    data = response.json()
    # data = json.loads(response.json())

    for attr in data:
        print(attr, data[attr])

    
move("s")

print(f"api key = {os.environ['API_KEY']}")