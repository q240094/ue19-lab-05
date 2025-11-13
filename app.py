import requests

url = "https://official-joke-api.appspot.com/jokes/programming/random"

print("Fetching joke…")
resp = requests.get(url)

if resp.status_code == 200:
    jokes = resp.json()
    joke = jokes[0]    # this API returns a list, so we take the first joke
    print("? ", joke.get("setup"))
    print("! ", joke.get("punchline"))
else:
    print("HTTP Error:", resp.status_code)
