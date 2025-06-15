import requests

url = "https://example.com"
response = requests.get(url)

for header, value in response.headers.items():
    print(f"{header}: {value}")
