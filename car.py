from mesh_geolocate import GeoData
from medium_manager import MediumManager

class Car:
    
    def __init__(self, medium: MediumManager):
        self.geo_data = GeoData(0, 0, 0)
        