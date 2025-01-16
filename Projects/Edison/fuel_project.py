# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 06:54:58 2025

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/data/qld_fuel.csv")
print(df)


# %%
# initial exploration
df.columns

df.info()

df.head()

df["Fuel_Type"]

pd.unique(df["Fuel_Type"])

df.describe()

df["Fuel_Type"].describe()

pd.unique(df["Site_Suburb"])

df["Site_Suburb"].describe()

pd.unique(df["Site_State"])

df["Site_State"].describe()


df[5 : 10]

pd.unique(df["Site_Name"])

df["Site_Name"].describe()

df.dtypes

df["Price"].describe()

df["Site_Brand"].describe()

# %%
# summaries
gb = df.groupby("Fuel_Type")

avg_fuel_by_price = gb["Price"].agg("mean")

plt.ion()
avg_fuel_by_price.plot()
plt.show()

# Ensure reasonable heights
df = df[ (500 < df["Price"]) & (df["Price"] < 4000)]

df["unit_price"] = df["Price"] / 1000

df.to_csv("data/filtered_fuel.csv")

sns.catplot(data = df, x = "Fuel_Type", y = "Price")
plt.show()


sns.catplot(data = df, x = "Site_State", y = "Fuel_Type")
plt.show()


# Remove unleaded Fuel_type
df1 = df[df["Fuel_Type"] != "Unleaded"]

sns.catplot(data = df1, x = "Site_State", y = "Fuel_Type")
plt.show()

# Remove unknown Site_Brand
df2 = df[df["Site_Brand"] != "Unknown"]

sns.catplot(data = df2, x = "Site_State", y = "Site_Brand", kind = "bar")
plt.show()


sns.displot(data = df, x = "Price", hue = "Fuel_Type", kind = "kde")
plt.show()

sns.displot(data = df, x = "unit_price", hue = "Fuel_Type", kind = "kde")
plt.show()

sns.catplot(data=df, x="unit_price", y="Fuel_type")
plt.show()
# %%

import pandas as pd
fuel = pd.read_csv("data/qld_fuel.csv")
import geopandas 
fuel_geo = geopandas.GeoDataFrame(fuel, geometry = geopandas.points_from_xy(x = fuel.Site_Longitude, y = fuel.Site_Latitude)) 
fuel_geo.plot()

# %%
import plotly.express as px
figure = px.scatter(data_frame = df, x = "Fuel_Type", y = "unit_price", color = "Site_State",
           facet_col = "Site_State", hover_name = "Site_Brand",
           hover_data = "Site_Suburb")

figure.write_html("fuel.html")

# %%
#| title: "Location of stations"
#| color: primary
import pandas as pd
fuel = pd.read_csv("data/qld_fuel.csv")
import geopandas 
fuel_geo = geopandas.GeoDataFrame(fuel, geometry = geopandas.points_from_xy(x = fuel.Site_Longitude, y = fuel.Site_Latitude)) 
fuel_geo.plot()