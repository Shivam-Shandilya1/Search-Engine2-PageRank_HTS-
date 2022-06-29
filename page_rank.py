import networkx as nx
import random
import numpy as np

def pagerank(G, alpha=0.90, personalization=None,
             max_iter=100, tol=1.0e-6, nstart=None, weight='weight',
             dangling=None):
    
    if len(G) == 0:
        return {}
 
    if not G.is_directed():
        D = G.to_directed()
    else:
        D = G
 
    # Create a copy in stochastic form
    W = nx.stochastic_graph(D, weight=weight)
    N = W.number_of_nodes()
 
    # Choose fixed starting vector if not given
    if nstart is None:
        x = dict.fromkeys(W, 1.0 / N)
    else:
        # Normalized nstart vector
        s = float(sum(nstart.values()))
        x = dict((k, v / s) for k, v in nstart.items())
 
    if personalization is None:
 
        # Assign uniform personalization vector if not given
        p = dict.fromkeys(W, 1.0 / N)
    else:
        missing = set(G) - set(personalization)
        if missing:
            raise nx.NetworkXError('Personalization dictionary '
                                'must have a value for every node. '
                                'Missing nodes %s' % missing)
        s = float(sum(personalization.values()))
        p = dict((k, v / s) for k, v in personalization.items())
 
    if dangling is None:
 
        # Use personalization vector if dangling vector not specified
        dangling_weights = p
    else:
        missing = set(G) - set(dangling)
        if missing:
            raise nx.NetworkXError('Dangling node dictionary '
                                'must have a value for every node. '
                                'Missing nodes %s' % missing)
        s = float(sum(dangling.values()))
        dangling_weights = dict((k, v/s) for k, v in dangling.items())
    dangling_nodes = [n for n in W if W.out_degree(n, weight=weight) == 0.0]
 
    # power iteration: make up to max_iter iterations
    for _ in range(max_iter):
        xlast = x
        x = dict.fromkeys(xlast.keys(), 0)
        danglesum = alpha * sum(xlast[n] for n in dangling_nodes)
        for n in x:
 
            # this matrix multiply looks odd because it is
            # doing a left multiply x^T=xlast^T*W
            for nbr in W[n]:
                x[nbr] += alpha * xlast[n] * W[n][nbr][weight]
            x[n] += danglesum * dangling_weights[n] + (1.0 - alpha) * p[n]
 
        # check convergence, l1 norm
        err = sum([abs(x[n] - xlast[n]) for n in x])
        if err < N*tol:
            return x
    raise nx.NetworkXError('pagerank: power iteration failed to converge '
                        'in %d iterations.' % max_iter)
    
# Sort the nodes
def nodes_sorted(g, points):
    t = np.array(points)
    t = np.argsort(-t)
    return t
  
# Distribute points randomly in a graph
def random_Walk(g):
    rwp = [0 for i in range(g.number_of_nodes())]
    nodes = list(g.nodes())
    r = random.choice(nodes)
    rwp[r] += 1
    neigh = list(g.out_edges(r))
    z = 0
      
    while (z != 10000):
        if (len(neigh) == 0):
            focus = random.choice(nodes)
        else:
            r1 = random.choice(neigh)
            focus = r1[1]
        rwp[focus] += 1
        neigh = list(g.out_edges(focus))
        z += 1
    return rwp
  
  
# Main
# 1. Create a directed graph with N nodes
g = nx.DiGraph()
N = int(input("Enter Number of Node: "))
g.add_nodes_from(range(N))
  
# 2. Add directed edges in graph
print("Add Edge until take -1 as input in both")
flag = True
while flag:
    from_edge = int(input("Edge from: "))
    to_edge = int(input("Edge to: "))
    if(from_edge!=-1 and to_edge!=-1):
        g.add_edge(from_edge,to_edge)
        print("Edge from",from_edge,"to",to_edge,"have been drawn.")
    else:
        flag = False
# 3. perform a random walk
points = random_Walk(g)
  
# 4. Get nodes rank according to their random walk points
sorted_by_points = nodes_sorted(g, points)
print("PageRank using Random Walk Method")
print(sorted_by_points)
  
# p_dict is dictionary of tuples
p_dict = nx.pagerank(g)
p_sort = sorted(p_dict.items(), key=lambda x: x[1], reverse=True)
  
print("PageRank using pagerank method")
for i in p_sort:
    print(i[0], end=", ")


