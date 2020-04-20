from pyproj import Proj
import math

class SinusoidalCoordinate():
    """
    Converts latitude and longitude in degrees to MODIS Sinusoidal grid coordinates.
    """
    def __init__(self):

        self.CELLS = 2400
        self.VERTICAL_TILES = 18
        self.HORIZONTAL_TILES = 36
        self.EARTH_RADIUS = 6371007.181
        self.EARTH_WIDTH = 2 * math.pi * self.EARTH_RADIUS

        self.TILE_WIDTH = self.EARTH_WIDTH / self.HORIZONTAL_TILES
        self.TILE_HEIGHT = self.TILE_WIDTH
        self.CELL_SIZE = self.TILE_WIDTH / self.CELLS
        self.MODIS_GRID = Proj(f'+proj=sinu +R={self.EARTH_RADIUS} +nadgrids=@null +wktext')

    def get_modis_grid_coord(self, latitude, longitude):
        x, y = self.MODIS_GRID(longitude, latitude)
        h = (self.EARTH_WIDTH * 0.5 + x) / self.TILE_WIDTH
        v = -(self.EARTH_WIDTH * 0.25 + y - self.VERTICAL_TILES  * self.TILE_HEIGHT) / self.TILE_HEIGHT
        return int(h), int(v)

