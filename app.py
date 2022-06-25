# Import required modules
from matplotlib import style
import numpy as np
import pandas as pd
import seaborn as sns
import shapefile as shp
import matplotlib.pyplot as plt

# Initialise visualisation set
sns.set(style="whitegrid", palette="pastel", color_codes=True)
sns.mpl.rc("figure", figsize=(10, 6))

# Open the vector map
shp_path = "./data/County.shp"
sf = shp.Reader(shp_path)

print(len(sf.records()))
