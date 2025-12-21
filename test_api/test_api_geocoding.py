import requests
import json
import csv

url = "https://nominatim.openstreetmap.org/search"
params = {
    "q": "Place Saint-Michel, Paris",
    "format": "json",
    "limit": 5
}
headers = {
    "User-Agent": "Rutafem-App/1.0"
}

response = requests.get(url, params=params, headers=headers)
data = response.json()

# Sauvegarde JSON
with open("nominatim_addresses.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Sauvegarde CSV (pour Excel)
if data:
    with open("nominatim_addresses.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)

print("✅ Données Nominatim récupérées")
