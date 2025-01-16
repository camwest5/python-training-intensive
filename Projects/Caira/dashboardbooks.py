# %% [markdown]
# ---
# title: Goodreads
# author: Caira
# date: today 
# format: 
#    dashboard: 
#           theme: solar 
#           scrolling: true
# --- 

# %%

import pandas as pd 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio

# %%

book_raw = pd.read_csv("data/goodreads_books.csv")

book = book_raw.copy() 


# %% 

#| output: false

book["publication_date"] = pd.to_datetime(book["publication_date"])



book["sum"] = book["ratings_count"] * book["average_rating"]

book["rating_range"] =  pd.cut(book["average_rating"], [-1,0.00,0.99, 1,1.99, 2,2.99, 3,3.99, 4,4.99, 5])

# %% [markdown]

"""
## Row {.fill}
"""

# %%


#| title: "How the Publication Year of Books has an Influence on its GoodReads Ratings."

px.scatter(data_frame = book, x = "publication_date", y = "sum", color = 'rating_range', 
            hover_name = "title", hover_data = ["average_rating", "authors"],
            labels={
                     "publication_date": "Publication Year",
                     "sum": "Sum of Ratings",
                     "rating_range": "Range"
                 })

# %% [markdown]

"""
## Row {.fill}
"""


# %% [markdown]

"""
## Table
"""

# %%

#| title: "A glimpse of the data"
book.head(4) 


# %% [markdown]

"""
## Row {.fill}
"""


# %%

#| content: valuebox
#| title: "Launched in"
#| icon: cake-fill
#| color: light
#| font-size: 1
"January 2007"

# %% [markdown]

"""
## Row {.flow}
"""


# %%

#| content: valuebox
#| title: "Founded By"
#| icon: pencil-square
#| color: light
"Otis Chandler"

# %%

#| content: valuebox
#| title: "and"
#| icon: pencil-square
#| color: light
"Elizabeth Khuri Chandler"
























