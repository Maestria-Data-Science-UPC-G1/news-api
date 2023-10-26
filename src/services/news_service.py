import services.graph as graph
import requests
import pandas as pd
import os
from flask import jsonify
from app import df
from entities.schemas import SimilarNode, Node
import re
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_graph(query):

    if query == "":
        return jsonify({"data": {"nodes": [], "links": []}})

    api_key = os.getenv('API_KEY')#'d53adf8af18a46b09393a3074acf2dcc'
    '''
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
    '''
    print(f"Iniciando busqueda con un dataframe total de {len(df)} articulos")
    pattern = r"\b{}\b".format(re.escape(query))
    df_resultados = df[df['text'].str.contains(pattern, case=False)]
    
    df_resultados = df_resultados.reset_index(drop=True)
    print(f"Se encontraron {len(df_resultados)} articulos")

    if len(df_resultados) == 0:
        return jsonify({"data": {"nodes": [], "links": []}})

    nodes, links, links_json, similar_nodes = graph.generate_similarity_pairs(df_resultados)

    ranks = graph.get_pagerank(links)
    print(f"Cantidad de Ranks: {len(ranks)}")
    print(f"Cantidad de Nodos: {len(nodes)}")

    sorted_nodes = sorted(nodes, key=lambda x: ranks[x[0]], reverse=True)
    nodes_json = [Node(*tupla).__dict__() for tupla in sorted_nodes]

    for node in nodes_json:
        node_id = node['id']
        if node_id in similar_nodes:
            nodes = [SimilarNode(*similar).__dict__() for similar in similar_nodes[node_id]]
            node['similar'] = nodes
    #print(f"Nodes: {sorted_nodes}")
    data = {
        "data": {
            "nodes": nodes_json,
            "links": links_json
        }
    }

    return jsonify(data)

def extract_source_data(source_json):
    return source_json['id'], source_json['name']

