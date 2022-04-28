import requests

url = "http://127.0.0.1:5000/salary"

response = requests.post(url, json={'yearsExperience': 1.8})
print(response.json())