import requests

def get_distance_km(start: tuple[float, float], end: tuple[float, float]) -> float:
    # start = (lat, lon), end = (lat, lon)
    url = (
        f"http://router.project-osrm.org/route/v1/driving/"
        f"{start[1]},{start[0]};{end[1]},{end[0]}"
        f"?overview=false"
    )

    r = requests.get(url)
    data = r.json()

    route = data["routes"][0]
    distance_km = route["distance"] / 1000
    return distance_km
