import services.graph as graph
import requests
import pandas as pd
import os
from flask import jsonify

def generate_graph(query):
    if query == "":
        return jsonify({"data": {"nodes": [], "links": []}})
    
    api_key = os.getenv('API_KEY')#'d53adf8af18a46b09393a3074acf2dcc'

    api_url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}&from=2023-10-07&to=2023-10-14&language=en&sortBy=popularity"
    response = requests.get(api_url)

    
    totalResults = response.json()['totalResults']

    if totalResults == 0:
        return jsonify({"data": {"nodes": [], "links": []}})

    print(f"totalResults: {totalResults}")

    df_articles = pd.DataFrame(response.json()['articles'])
    df_articles[['source_id', 'source_name']] = df_articles['source'].apply(extract_source_data).apply(pd.Series)
    df_articles = df_articles.drop('source', axis=1)

    links, nodes = graph.generate_similarity_pairs(df_articles)

    data = {
        "data": {
            "nodes": nodes,
            "links": links
        }
    }

    return jsonify(data)

def extract_source_data(source_json):
    return source_json['id'], source_json['name']

