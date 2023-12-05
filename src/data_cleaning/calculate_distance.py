from math import radians, cos, sin, asin, sqrt


# Haversine function to calculate distance
def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate distance between two points on earth based on latitude and longitude
    """
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 3956

    return round(c * r)
