import networkx as nx
import matplotlib.pyplot as plt
import json
G = nx.Graph()
with open("dict.json") as g:
    x = json.load(g)
def graphtrie(trie):
    for item in trie['child']:
        if item['child'] != None:
            G.add_node(item["val"])
            G.add_edge(trie['val'],item['val'])
            graphtrie(item)
            
graphtrie(x)
nx.draw_circular(G, with_labels=True, font_weight='bold')
plt.show()