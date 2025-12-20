import requests

def geocode(address):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "Rutafem-App/1.0" 
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    if not data:
        return None

    lat = float(data[0]["lat"])
    lon = float(data[0]["lon"])
    return lat, lon


# TEST
lat, lon = geocode("Place Saint-Michel, Paris")
print(lat, lon)
