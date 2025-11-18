import requests

# Correct endpoint (no /random, and "Programming" is capitalized)
url = "https://v2.jokeapi.dev/joke/Programming"

print("Fetching joke…")
resp = requests.get(url)

if resp.status_code == 200:
    data = resp.json()
    print("💡")
    if data.get("type") == "twopart":
        print("? ", data.get("setup"))
        print("! ", data.get("delivery"))
    else:  # single joke
        print("! ", data.get("joke"))

else:
    print("HTTP Error:", resp.status_code)

