import networkx as nx
G = nx.read_gpickle("./web_graph.gpickle")

root_list = []

def set_root(query):
    for i in range(0,len(G.nodes)):
        if(query in G.nodes[i]['page_content']):
            root_list.append(i)
            
# set_root("Phelps")            
# print("ROOT SET:")
# if root_list:
#         print(root_list)
# else:
#         print("Hi")