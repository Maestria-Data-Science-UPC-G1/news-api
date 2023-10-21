from flask import jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from entities.schemas import Link, Node
import networkx as nx

def generate_similarity_pairs(dataframe):
    vectorizer = CountVectorizer(binary=True)
    X = vectorizer.fit_transform(dataframe['title'])

    umbral = 0.37

    # Calcular la similitud de Jaccard
    jaccard_sim = cosine_similarity(X)

    # Encontrar las parejas similares
    similar_pairs = []
    links_json = []
    #nodes = []
    links= []
    nodes = []
    for i in range(len(dataframe)):
        for j in range(i + 1, len(dataframe)):
            if jaccard_sim[i, j] >= umbral:
                #node1 = Node(i, dataframe.loc[i, 'title'], dataframe.loc[i, 'content'], dataframe.loc[i, 'url'], dataframe.loc[i, 'author'], dataframe.loc[i, 'description'], dataframe.loc[i, 'publishedAt'], dataframe.loc[i, 'source_name'])
                #node2 = Node(j, dataframe.loc[j, 'title'], dataframe.loc[j, 'content'], dataframe.loc[j, 'url'], dataframe.loc[j, 'author'], dataframe.loc[j, 'description'], dataframe.loc[j, 'publishedAt'], dataframe.loc[j, 'source_name'])
                #nodes.append(node1.__dict__())
                #nodes.append(node2.__dict__())
                link = Link(i, j, jaccard_sim[i, j])
                links_json.append(link.__dict__())
                links.append((i, j))
                nodes.append((i, dataframe.loc[i, 'title'], dataframe.loc[i, 'content'], dataframe.loc[i, 'url'], dataframe.loc[i, 'author'], dataframe.loc[i, 'description'], dataframe.loc[i, 'publishedAt'], dataframe.loc[i, 'source_name']))
                nodes.append((j, dataframe.loc[j, 'title'], dataframe.loc[j, 'content'], dataframe.loc[j, 'url'], dataframe.loc[j, 'author'], dataframe.loc[j, 'description'], dataframe.loc[j, 'publishedAt'], dataframe.loc[j, 'source_name']))
                similar_pairs.append((dataframe.loc[i, 'title'], dataframe.loc[j, 'title'], jaccard_sim[i, j], i, j))

    print(f"Nodos antes del corte: {len(nodes)}")
    #nodes = list({node['id']: node for node in nodes}.values())
    # lo mismo que hice para nodes quiero hacerlo para nodes2
    nodes = list({node[0]: node for node in nodes}.values())
    print(f"Nodos despues del corte: {len(nodes)}")
    print(f"Links : {len(links)}")

    return nodes, links, links_json

# pagerank
def get_pagerank(links):
    g = nx.Graph()
    #g.add_nodes_from(nodes)
    g.add_edges_from(links)

    pagerank = nx.pagerank(g) # calcular el pagerank de todos los nodos
    ranks = [(k,v) for k,v in sorted(pagerank.items(), key=lambda item:-item[1])]
    print(f"ranks: {ranks}")
    
    return pagerank
