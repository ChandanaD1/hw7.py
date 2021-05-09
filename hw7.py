# data visualization

import pandas as pd
import plotly.express as px

df = pd.read_csv("hw7.csv")
print(df)

graph = px.scatter(df, x = "date", y = "cases", color = "country")
graph.show()