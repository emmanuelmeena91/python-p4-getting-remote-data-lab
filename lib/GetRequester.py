import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response = requests.get(self.url)
        data = json.loads(response.text)
        return data

# Example usage
url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

# Create an instance of GetRequester with the URL
requester = GetRequester(url)

# Get the response body
response_body = requester.get_response_body()
print(response_body)

# Load the JSON data
json_data = requester.load_json()
print(json_data) 