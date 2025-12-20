import requests

# -------- SOURCE 1 : ADRESSE -> COORDONNEES --------
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
        raise Exception("Adresse non trouvée")

    lat = float(data[0]["lat"])
    lon = float(data[0]["lon"])
    return lat, lon


# -------- SOURCE 2 : DISTANCE (OSRM) --------
def get_distance_km(start, end):
    url = (
        f"http://router.project-osrm.org/route/v1/driving/"
        f"{start[1]},{start[0]};{end[1]},{end[0]}"
    )

    response = requests.get(url)
    data = response.json()

    route = data["routes"][0]
    distance_km = route["distance"] / 1000
    return distance_km


# -------- SOURCE 3 : COUT CARBURANT --------
def fuel_cost(distance_km, consumption_l_100km=5, fuel_price=1.85):
    return (distance_km / 100) * consumption_l_100km * fuel_price


# -------- TEST COMPLET --------
departure = "Place Saint-Michel, Paris"
arrival = "Place Charles de Gaulle, Paris"

start_coords = geocode(departure)
end_coords = geocode(arrival)

distance = get_distance_km(start_coords, end_coords)
cost = fuel_cost(distance)

print("Distance (km):", round(distance, 2))
print("Coût carburant (€):", round(cost, 2))
