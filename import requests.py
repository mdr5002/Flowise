import requests

API_URL = "http://localhost:3000/api/v1/prediction/dc842994-11df-43ab-98e4-1ded620c0b4f"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()
    
output = query({
    "question": "Hey, what do you think I should do for work?",
})
