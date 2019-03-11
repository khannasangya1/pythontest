import requests
import json

url = "https://reqres.in/api/users"

file = open('//home//ashwani//apis//NewUser.json','r')
json_input = file.read()
json_request = json.loads(json_input)


response = requests.post(url,json_request)
print(response.content)
