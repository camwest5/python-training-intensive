# %% [markdown]
#---
#title: Analyzing the Relationship between Ratings and Reviews for Books
#author: Nurul Najihah
#date: 2025-01-15
#warning: false
#format:
#   dashboard:
#       theme: quartz
#---

# %%

import pandas as pd
df = pd.read_csv("books.csv")



# %%
#| echo: false
#| fig-cap: "Relationship between two variables"

import seaborn as sns
sns.catplot(data = df,
            x = 'ratings_count',
            y = 'text_reviews_count')

# %% [markdown]
"""
## Table
"""

#%%
#| title: "An Overview of the Data"
df

#%%
#| content: valuebox
#| title: "Correlation value"
#| icon: bookmark-heart
#| color: primary
0.86598

#%%
#| content: valuebox
#| title: "Maximum ratings count"
#| icon: book-half
#| color: secondary
df["ratings_count"].max().item()

#%%
#| content: valuebox
#| title: "Maximum Book Review"
#| icon: chat-right-dots
#| color: info
df["text_reviews_count"].max().item()



