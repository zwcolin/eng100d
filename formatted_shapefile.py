import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import contextily as ctx 
import geopandas as gpd 
import os 
from mpl_toolkits.axes_grid1 import make_axes_locatable

path = "tl_2021_06_tract.zip"
df = gpd.read_file(path)
df = df[(df.COUNTYFP == "073")]
print(df)

census_tracts = ["30.01", "30.04", "31.11", "33.04", "33.05", "34.04", "33.03", "36.01", "36.02",
                 "35.01", "35.02", "40", "39.01", "39.02", "47", "48", "49", "50", "51.01", "51.02", "51.03"]

pz_df =df[df['NAME'].isin(census_tracts)]
print(pz_df)
pz_df.plot()

df.plot()
