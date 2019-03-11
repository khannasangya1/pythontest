import requests
import json



url = "https://reqres.in/api/users/2"

file = open('//home//ashwani//apis//NewUser.json','r')
json_input = file.read()

json_request = json.loads(json_input)

response = requests.put(url,json_request)

response_json = json.loads(response.text)

print(response.content)