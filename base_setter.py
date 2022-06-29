from root_setter import set_root,root_list 
import networkx as nx

G = nx.read_gpickle("./web_graph.gpickle")
base_list = {}
base_li = []
base_map = {}
base_map_set = {}
def set_base():
    for edge in G.edges():
        base_map_set[edge[0]] = []
    for edge in G.edges():
        if(edge[1] not in base_map_set[edge[0]]):
            base_map_set[edge[0]].append(edge[1])
    for edge in G.edges():
        base_map[edge[0]] = []
    for edge in G.edges():
        if(edge[1] not in base_map[edge[0]]):
            base_map[edge[0]].append(edge[1])
        if(edge[0] not in base_map[edge[1]]):
            base_map[edge[1]].append(edge[0])
    for root in root_list:
        for r in base_map[root]:
            if(root not in base_li):
                base_li.append(root)
            if(r not in base_li):
                base_li.append(r)
    for base in base_li:
        base_list[base] = []
    for base in base_li:
        for b in base_map_set[base]:
            if(b in base_li):
                base_list[base].append(b) 
        
        
# set_root("Sports")
# set_base()
# for key in base_map:
#     print(key,"->",base_map[key])



# print(base_list)
    # for key in base_map:
    #     print(key,'->',base_map[key])
    # for k in root_list:
    #     base_list.append(k)
    #     base_list.append(base_map[k])
    #     for v in base_map[k]:
    #         if v not in base_list:
    #             base_list.append(base_map[v])
        # else:
        #     print(edge[0])
    
    # print(base_list)

# set_root("Phelps")
# set_base()
# print(base_map_set)
# print(base_li)
# print(base_list)