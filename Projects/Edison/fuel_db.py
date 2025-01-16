# %% [markdown]
# ---
# title: Fuel Comsuption
# author: Edison Vargas
# date: today
# format: 
#   dashboard:
#       theme: journal
# ---


# %%
import pandas as pd

df = pd.read_csv("data/data/filtered_fuel.csv")

# %% [markdown]
"""
## Visualisations  {height=65%}
"""
# %%
#| title: "Comparison Unit price vs Fuel type"
import seaborn as sns

sns.displot(data = df, 
            x = "unit_price", 
            hue = "Fuel_Type", 
            kind = "kde")
# %% 
#| title: "Comparison Price comsuption per State"
import plotly.express as px
px.scatter(data_frame = df, x = "Fuel_Type", y = "unit_price", color = "Site_State",
           facet_col = "Site_State", hover_name = "Site_Brand",
           hover_data = "Site_Suburb")

# %%
#| title: "Name of stations vs State"
#| color: primary
import seaborn as sns
sns.catplot(data = df, 
            x = "Site_State", 
            y = "Site_Brand", 
            kind = "bar")

# %% [markdown]
"""
## Table
"""

# %% 
#| title: "A glimpse of the data"
df


# %%
#| title: "Statistics unit price"
#| color: secondary
df["unit_price"].describe()

# %%
#| content: valuebox
#| title: "Average price $:"
#| icon: trophy
#| color: primary
float(df["unit_price"].mean())

