#import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
import pyfpgrowth
import networkx as nx
#from sklearn import cluster

import collections
import itertools

#df = pd.read_csv('pokemon_go.xlsm', encoding = "shift-jis")
df = pd.read_excel('pokemon_go.xlsm')
print(df)
df = df.dropna(subset=['先発']).dropna(subset=['控え1']).dropna(subset=['控え2'])
df_s = df[df['リーグ'] == 'S']
df_h = df[df["リーグ"] == 'H']

df_s_member = df_s.loc[:,['先発','控え1','控え2']]
df_h_member = df_h.loc[:,['先発','控え1','控え2']]

list_s_member = df_s_member.values.tolist()
list_h_member = df_h_member.values.tolist()

list_member = [list_s_member, list_h_member]
leage_name_list = ['super', 'hyper']
dic_of_list = {'super': list_s_member, 'hyper': list_h_member}

s_count =collections.Counter(itertools.chain.from_iterable(list_s_member)).most_common(50)
h_count =collections.Counter(itertools.chain.from_iterable(list_h_member)).most_common(50)

dic_of_count = {'super': s_count, 'hyper': h_count}

np.random.seed(1)

for leage_name in leage_name_list:
    for k_value in [0.5]  :  
        list_member = dic_of_list[leage_name]
        member_count = dic_of_count[leage_name]
        dict_mem_cnt = dict(member_count)
        print(member_count)

        list_member_flatten = list(itertools.chain.from_iterable(list_member))
        list_member_flatten = list(set(list_member_flatten))
        
        #G = nx.Graph()
        '''
        for member, count in member_count:
            G.add_node(member, node_size = count *3)
            #print(member,":", count)

            #G.add_nodes_from([(member, {"count":count} )for member, count in member_count])
        '''
        '''z
        for cnt_min in range(1,3):

            for member1, member2 in itertools.combinations(list_member_flatten,2):
                cnt = len([i for i in list_member if member1 in i if member2 in i])
                ##print(member1)
                #print(member2)
                ##print(cnt)
                import sys

                if cnt > cnt_min:
                    print(member1,":", member2,":", cnt)
                    G.add_edge(member1, member2, weight=cnt)
            
            pos = nx.spring_layout(G, k=0.3)
            #node_size = [ d["count"]*20 for (n,d) in G.nodes(data=True)]
            #print(node_size)

            #nx.draw_networkx_nodes(G, pos, node_color="w",alpha=0.6, node_size=node_size)
            #nx.draw_networkx_labels(G, pos, fontsize=14, font_family="Yu Gothic", font_weight="bold")

        '''
        
        for i in range(1,4):
            
            patterns = pyfpgrowth.find_frequent_patterns(list_member, i)
            G = nx.Graph()
            #G.add_nodes_from([(member, {"count":count} )for member, count in list_member])

            #G.add_nodes_from([(list_member)])
            #print('patterns')
            #print(patterns)
            pat_list = []
            for key in patterns.keys():
                if len(key) == 2 or len(key) == 3 :
                    for num_key in range(len(key)):
                        pat_list.append(key[num_key])
            pat_list = list(set(pat_list))
            #print(pat_list)

            for key in patterns.keys():
                if len(key) == 2 or len(key) == 3 :
                    G.add_path(key)
                    #print(key)

            '''
            for key in patterns.keys():
                if len(key) == 1:
                    print("key")
                    print(key[0])
                    
                    count_ = dict_mem_cnt[key[0]]
                    print("key: ", key[0], " count:", count_)
                    G.edges[key[0]]['weight']
            '''

            pr = nx.pagerank(G)
            print(pr)
            plt.figure(figsize=(20,20))
            pos = nx.spring_layout(G, k=k_value)
            nx.draw_networkx(G, node_color=list(pr.values()), cmap=plt.cm.Reds, font_size=15, node_size =5000, font_family="Yu Gothic")
            
            plt.savefig(leage_name + "/" + leage_name + str(i)+"_" +str(k_value) + '_.png')


        
            '''
            for members in list_member:
                for node0, node1 in itertools.combinations(members, 2):
                    if not G.has_node(node0) or not G.has_node(node1):
                        continue
                    if G.has_edge(node0, node1):
                        G.edges[node0][node1]["weight"] += 1
                    else:
                        G.add_edge(node0, node1, weight=1.0)
            '''