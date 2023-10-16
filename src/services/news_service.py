import services.graph as graph
import requests
import pandas as pd
from flask import jsonify

def generate_graph(query):
    if query == "":
        return jsonify({"data": {"nodes": [], "links": []}})

    api_url = f"https://newsapi.org/v2/everything?q={query}&apiKey=d53adf8af18a46b09393a3074acf2dcc&from=2023-10-07&to=2023-10-14&language=en&sortBy=popularity"
    response = requests.get(api_url)
    #df = pd.DataFrame(response.json())
    df_articles = pd.DataFrame(response.json()['articles'])
    df_articles[['source_id', 'source_name']] = df_articles['source'].apply(extract_source_data).apply(pd.Series)
    df_articles = df_articles.drop('source', axis=1)

    links, nodes = graph.generate_similarity_pairs(df_articles)
    #print(similar_pairs)


    data = {
        "data": {
            "nodes": nodes,
            "links": links
        }
    }

    ##return similar_pairs#graph.generate_graph()
    return jsonify(data)

def extract_source_data(source_json):
    return source_json['id'], source_json['name']

