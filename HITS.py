import networkx as nx
import numpy as nump
from root_setter import set_root,root_list
from base_setter import set_base,base_map,base_list,base_li
G = nx.read_gpickle('web_graph.gpickle')
print("Entered Directed graph has " + str(G.number_of_nodes())+" nodes and " + str(G.size()) + " edges")

query = input('Your query:')
set_root(query)
print("Root List: ",root_list)
set_base()
print("Base List: ",base_li)
authority_matrix = nump.zeros(100)

for i in range(0, G.number_of_nodes()):
    content = G.nodes[i]['page_content']
    arrA = content.replace(":",";").replace(";",",").replace(","," ").split()
    if query in arrA:
        authority_matrix[i] = 1
        break

adjacency_matrix = nx.to_numpy_array(G)
authority_matrix = nump.array(authority_matrix)


hub_matrix = nump.dot(authority_matrix, adjacency_matrix)


hub_transpose = nump.dot(authority_matrix, adjacency_matrix.T)


arrB = nump.add(authority_matrix, nump.add(hub_matrix, hub_transpose))

arrC = []

for i in range(0, G.number_of_nodes()):
    if(arrB[i]):
        # Adding the index elements to arrC
        arrC.append(i)
arrD = []
# creating a subgraph of G
arrD = arrC
subG = nx.subgraph(G, arrC)
arrE = nx.to_numpy_array(subG)

hubscore = nump.ones(len(arrC))
authscore = nump.ones(len(arrC))
hubscoresum = 0
authscoresum = 0
for i in range(len(hubscore)):
    hubscoresum += hubscore[i]
for i in range(len(hubscore)):
    hubscore[i] = hubscore[i]/hubscoresum
for i in range(len(authscore)):
    authscoresum += hubscore[i]
for i in range(len(hubscore)):
    authscore[i] = authscore[i]/authscoresum

for count in range(0, 10000):
    hubscore = nump.dot(arrE, authscore)
    authscore = nump.dot(arrE.T, hubscore)
    hubscore = hubscore/sum(hubscore)
    authscore = authscore/sum(authscore)

arrD = list(subG.nodes)


print("\nNode\tHub Values:")
index = 0
for x in hubscore:
    x = round(x,6)
    print(arrD[index], end="\t")
    #print(x, end="\n")
    print(str(x)+"\n")
    index = index+1

print("\nNode\tAuthority Values:")
index = 0
for x in authscore:
    print(arrD[index], end="\t")
    print(round(x,6), end="\n")
    index = index+1