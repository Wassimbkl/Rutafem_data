from src.geocoding import geocode
from src.routing import get_distance_km
from src.fuel import fuel_cost
from src.tolls import has_toll_on_route

def compute_price(
    departure: str,
    arrival: str,
    passengers: int,
    consumption_l_100km: float = 5.0,
    fuel_price_eur_l: float = 1.68,
    commission_eur: float = 15.0,
    toll_flat_eur: float = 0.0 # on a pas encore calculé le péage
) -> dict:
    if passengers <= 0:
        raise ValueError("passengers doit être >= 1")

    # 1) Geocode
    start = geocode(departure)
    end = geocode(arrival)

    # 2) Distance
    distance_km = get_distance_km(start, end)

    # 3) Carburant
    fuel_eur = fuel_cost(distance_km, consumption_l_100km, fuel_price_eur_l)

    # 4) Péage (free flow)
    has_toll = has_toll_on_route(start, end)
    toll_eur = toll_flat_eur if has_toll else 0.0

    # 5) Total
    total = fuel_eur + toll_eur + commission_eur
    per_passenger = total / passengers

    return {
        "departure": departure,
        "arrival": arrival,
        "distance_km": round(distance_km, 2),
        "fuel_eur": round(fuel_eur, 2),
        "has_toll": bool(has_toll),
        "toll_eur": round(toll_eur, 2),
        "commission_eur": round(commission_eur, 2),
        "total_eur": round(total, 2),
        "per_passenger_eur": round(per_passenger, 2),
    }
