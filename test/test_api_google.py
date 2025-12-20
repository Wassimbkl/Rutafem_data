import requests
import json

API_KEY = "AIzaSyDhKb8piPT4DVwM2rSab4l790gprqN9aL8"

url = "https://routes.googleapis.com/directions/v2:computeRoutes"

headers = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": API_KEY,
    "X-Goog-FieldMask": (
        "routes.distanceMeters,"
        "routes.duration,"
        "routes.travelAdvisory.tollInfo"
    )
}

body = {
    "origin": {
        "location": {
            "latLng": {
                "latitude": 48.8566,   # Paris
                "longitude": 2.3522
            }
        }
    },
    "destination": {
        "location": {
            "latLng": {
                "latitude": 45.7640,   # Lyon
                "longitude": 4.8357
            }
        }
    },
    "travelMode": "DRIVE",
    "routingPreference": "TRAFFIC_UNAWARE",
    "routeModifiers": {
        "avoidTolls": False
    }
}

response = requests.post(url, headers=headers, data=json.dumps(body))
data = response.json()

print(json.dumps(data, indent=2))
