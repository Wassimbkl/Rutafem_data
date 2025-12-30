import geopandas as gpd
from shapely.geometry import LineString

# On charge le GeoJSON UNE FOIS (global)
AUTOROUTES_FF = gpd.read_file("data/autoroutes-free-flow-fr.geojson").to_crs(epsg=2154)

def has_toll_on_route(
    start: tuple[float, float],
    end: tuple[float, float],
    buffer_m: int = 500
) -> bool:
    """
    start/end = (lat, lon)
    """
    # shapely attend (lon, lat)
    trajet = LineString([
        (start[1], start[0]),
        (end[1], end[0])
    ])

    trajet_gdf = gpd.GeoDataFrame(geometry=[trajet], crs="EPSG:4326").to_crs(epsg=2154)

    # zone tampon autour du trajet
    zone = trajet_gdf.buffer(buffer_m).iloc[0]

    return AUTOROUTES_FF.intersects(zone).any()
