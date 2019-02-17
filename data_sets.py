import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random

all_degrees = []
normalized_degrees = []

def plot(list_values,xlabel,ylabel,title):
	unique_degrees = list(sorted(set(list_values)))
	count_of_degrees = []
	for i in unique_degrees:
		x = all_degrees.count(i)
		count_of_degrees.append(x)
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.plot(unique_degrees,count_of_degrees)
	plt.show()

def draw(G, pos, measures, measure_name):
    
    nodes = nx.draw_networkx_nodes(G, pos, cmap=plt.cm.plasma, 
                                   node_color=list(measures.values()),
                                   nodelist=list(measures.keys()))
    nodes.set_norm(mcolors.SymLogNorm(linthresh=0.01, linscale=1))
    
    #labels = nx.draw_networkx_labels(G, pos)
    edges = nx.draw_networkx_edges(G, pos)

    plt.title(measure_name)
    plt.colorbar(nodes)
    plt.axis('off')
    plt.show()

def degree_centrality(G,pos):
	global all_degrees
	all_degrees = [val for (node, val) in G.degree()]
	plot(all_degrees,"Unique Degrees","Count Of Degrees","Degree_centrality")
	draw(G, pos, nx.degree_centrality(G), 'Degree Centrality')

def normalized_degree_centrality(G):
	global normalized_degrees
	n = len(all_degrees)
	v = 1/(n-1)
	for i in range(0,n):
		normalized_degrees.append(v*all_degrees[i])
	plot(all_degrees,"Unique Degrees","Count Of Degrees","Normalized Degree_centrality")

def eigenvector_centrality(G):
	centrality = nx.eigenvector_centrality(G).values()
	unique_degrees = list(sorted(set(centrality)))
	plot(centrality,"Unique Degrees","Count Of Degrees","EigenVector Centrality")

def betweenness_centrality(G):
	centrality = nx.betweenness_centrality(G);
	unique_degrees = list(sorted(set(centrality)))
	plot(centrality,"Unique Degrees","Count Of Degrees","betweenness_centrality")

def closeness_centrality(G):
	centrality = nx.closeness_centrality(G).values()
	unique_degrees = list(sorted(set(centrality)))
	plot(centrality,"Unique Degrees","Count Of Degrees","Closeness Centrality")

def katz_centrality(G):
	centrality = nx.katz_centrality(G)
	unique_degrees = list(sorted(set(centrality)))
	plot(centrality,"Unique Degrees","Count Of Degrees","Katz Centrality")

def page_rank(G):
	centrality=nx.pagerank(G)
	unique_degrees = list(sorted(set(centrality)))
	plot(centrality,"Unique Degrees","Count Of Degrees","Page Rank")

if __name__ == "__main__": 
	G = nx.Graph()
	for i in range(1,101):
		G.add_node(i)
	with open('ego-twitter/out.ego-twitter') as f:
		content = f.readlines()
	content = [x.strip() for x in content]
	for each in content:
		nums = [int(x) for x in each.split()]
		if((nums[0]<=100) & (nums[1]<=100) & (nums[0] != nums[1]) & (G.has_edge(nums[0],nums[1]) == 0)):
			G.add_edge(nums[0],nums[1])

	print(nx.info(G))
	nx.draw(G)
	plt.show()
	pos = nx.spring_layout(G)
	degree_centrality(G,pos)
	normalized_degree_centrality(G)
	eigenvector_centrality(G)
	betweenness_centrality(G)
	katz_centrality(G)
	page_rank(G)
