
import requests
import json
import jsonpath


url = "https://reqres.in/api/users?page=2"

response = requests.get(url)
print(response)

# Display response content

print(response.content)
print(response.headers)

# Validate status code
print(response.status_code)
assert response.status_code == 200

# Fetch response headers
print(response.headers)

# Fetch specific content from the header

print(response.headers.get('Date'))
print (response.headers.get('Server'))

# Fetch cookies

print(response.cookies)

# Fetch encoding

print(response.encoding)

# Fetch elapsed time
print(response.elapsed)

# Parse response to json format

json_response = json.loads(response.text)

# fetching data using jsonpath

pages = jsonpath.jsonpath(json_response,'total_pages')
print(pages[0])
for i in range(0,3):

  first_name = jsonpath.jsonpath(json_response,'data['+str(i)+'].first_name')
  print(first_name[0])