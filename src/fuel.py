def fuel_cost(distance_km: float, consumption_l_100km: float, fuel_price_eur_l: float) -> float:
    """
    distance_km : km
    consumption_l_100km : litres / 100km (ex: 5)
    fuel_price_eur_l : prix €/L (ex: 1.68)
    """
    return (distance_km / 100) * consumption_l_100km * fuel_price_eur_l
