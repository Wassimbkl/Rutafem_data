import requests
import json

# Coordonnées Paris -> Lyon
start = (2.3522, 48.8566)
end = (4.8357, 45.7640)

url = f"http://router.project-osrm.org/route/v1/driving/{start[0]},{start[1]};{end[0]},{end[1]}?overview=full&geometries=geojson"

response = requests.get(url)
data = response.json()

# Sauvegarde JSON
with open("osrm_route.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(" Données OSRM récupérées")
