#%% [markdown]
# ---
# title: The popular author
# author: Goodread  
# date: today
# format: 
#   dashboard: 
#       theme: sketchy
# --- 
# %%

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
df_raw = pd.read_csv('books.csv')

df = df_raw.copy()

df["publication_date"] = pd.to_datetime(df['publication_date'])
# %% [markdown]

"""
## Row {.fill}
"""

# %%
df['rating_range'] = pd.cut(df['average_rating'],[0,0.99,1,1.99,2,2.99,3,3.9,4,5])
px.scatter(data_frame= df, x='publication_date', 
           y='average_rating', 
           color='rating_range',
           labels= {'publication_date':'Publication year',
                    'average_rating': 'Star rating',
                    'rating_range': 'Range'},
           title= 'Rating popularity')

# %% [markdown]

"""
## Row {.fill}
"""
# %%
#| title: 'Average rating base on year'
df_filtered = df[df['average_rating'] > 4.5]
sns.relplot(data=df_filtered, x='publication_date', y='average_rating', kind= 'line')

# %%
#| title: 'Top publishers'
df_filtered = df[df['average_rating'] == 5.0]
df_new=df_filtered[['publisher']]
df_new
# %%
#| content: valuebox
#| title: 'Number of books that got 5 stars'
#| icon: book 
#| color: primary 
22
# %%
#| content: valuebox
#| title: 'Number of publishers that got the highest rated book'
#| icon: trophy-fill
#| color: secondary 
13







