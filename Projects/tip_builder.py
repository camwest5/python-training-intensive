import pandas as pd
import seaborn as sns

p = print

# # World pop
# df = pd.read_csv("data_sources/population.csv")

# input(df["Region"].unique())

# country = df[(df["Region"] == "United States of America") | (df["Region"].str.contains("Russia"))]
W
# fig = sns.relplot(country, x = "Year", y = "Net.Migration.Rate..per.1.000.population.", hue = "Region", kind = "line")

# fig.savefig("test.png")

# Coffee
df = pd.read_csv("data_sources/coffee_survey.csv")

p(df.info())



fig = sns.catplot(df, hue = "cups", x = "number_children",  kind = "bar", multiple = "stack")

fig.savefig("test.png")