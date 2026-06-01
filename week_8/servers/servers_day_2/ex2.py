import requests

def safe_get(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return None
    raise ValueError(response.status_code)


print(safe_get("https://try.org.il"))
