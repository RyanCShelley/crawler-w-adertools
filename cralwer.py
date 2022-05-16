# Install advertools

!pip install advertools

# Import Dependencies

import advertools as adv
from advertools import crawl
import pandas as pd

# Create Variable

site = "https://simplifiedsearch.net/"  #@param {type:"string"}

# Create Crawler

crawl(site, 'simp.jl', follow_links=True)
crawl_df = pd.read_json('simp.jl', lines=True)
crawl_df.head()

#View Comlumn Lists

columns = list(crawl_df)
columns

#Review JSON Type

json_df = crawl_df[['url', 'jsonld_@type' ]]
json_df

#Downlodad Files

from google.colab import files


json_df.to_csv("json_df.csv")
files.download('json_df.csv')

#Count JSON Types

json_counts = json_df['jsonld_@type'].value_counts()
json_counts = json_counts.reset_index()
json_counts

#Visualize the Data

!pip install plotly
import plotly.express as px

fig = px.bar(json_counts, x='index', y='jsonld_@type')
fig.show()
