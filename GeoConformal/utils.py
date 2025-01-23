import geopandas as gpd
import numpy as np
import pandas as pd


class GeoConformalResults:
    def __init__(self, geo_uncertainty: np.ndarray, uncertainty: float, coords: np.ndarray, pred: np.ndarray,
                 upper_bound: np.ndarray, lower_bound: np.ndarray, coverage_probability: float,
                 crs: str = 'EPSG:4326'):
        self.uncertainty = uncertainty
        self.geo_uncertainty = geo_uncertainty
        self.coords = coords
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound
        self.pred = pred
        self.coverage_probability = coverage_probability
        self.crs = crs

    def to_gpd(self) -> gpd.GeoDataFrame:
        geo_uncertainty_pd = pd.DataFrame(np.column_stack(
            [self.geo_uncertainty, self.pred, self.upper_bound, self.lower_bound, self.coords]))
        geo_uncertainty_pd.columns = ['geo_uncertainty', 'pred', 'upper_bound', 'lower_bound', 'x', 'y']
        geo_uncertainty_gpd = gpd.GeoDataFrame(geo_uncertainty_pd, crs=self.crs,
                                               geometry=gpd.points_from_xy(x=geo_uncertainty_pd.x,
                                                                           y=geo_uncertainty_pd.y))
        return geo_uncertainty_gpd