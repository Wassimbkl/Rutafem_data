import requests

def geocode(address: str) -> tuple[float, float]:
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": address, "format": "json", "limit": 1}
    headers = {"User-Agent": "Rutafem-App/1.0"}

    r = requests.get(url, params=params, headers=headers)
    data = r.json()

    if not data:
        raise ValueError(f"Adresse introuvable: {address}")

    lat = float(data[0]["lat"])
    lon = float(data[0]["lon"])
    return (lat, lon)  # (lat, lon)
