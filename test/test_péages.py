import geopandas as gpd
from shapely.geometry import LineString

# Charger les autoroutes free flow
autoroutes_ff = gpd.read_file(
    "data/autoroutes-free-flow-fr.geojson"
).to_crs(epsg=2154)  # mètres

# Trajet de test 
trajet = LineString([
    (0.732018, 47.452839),
    (0.742484, 47.448479)
])

trajet_gdf = gpd.GeoDataFrame(
    geometry=[trajet],
    crs="EPSG:4326"
).to_crs(epsg=2154)

#  Buffer autour du trajet (500 m = tolérance réaliste)
trajet_buffer = trajet_gdf.buffer(500)

# Test d’intersection ROBUSTE
has_toll = autoroutes_ff.intersects(
    trajet_buffer.iloc[0]
).any()

print("has_toll =", has_toll)
