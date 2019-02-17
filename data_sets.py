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

def normalized_degree_centrality(G,pos):
	global normalized_degrees
	n = len(all_degrees)
	v = 1/(n-1)
	for i in range(0,n):
		normalized_degrees.append(v*all_degrees[i])
	plot(all_degrees,"Unique Degrees","Count Of Degrees","Normalized Degree_centrality")

def eigenvector_centrality(G,pos):
	centrality = nx.eigenvector_centrality(G)
	unique_degrees = list(sorted(set(centrality)))
	plot(centrality,"Unique Degrees","Count Of Degrees","EigenVector Centrality")
	draw(G, pos,centrality, 'Eigen Vector Centrality')

def betweenness_centrality(G,pos):
	centrality = nx.betweenness_centrality(G);
	unique_degrees = list(sorted(set(centrality)))
	plot(centrality,"Unique Degrees","Count Of Degrees","betweenness_centrality")
	draw(G, pos,centrality, 'Betweenness Centrality')

def closeness_centrality(G,pos):
	centrality = nx.closeness_centrality(G)
	unique_degrees = list(sorted(set(centrality)))
	plot(centrality,"Unique Degrees","Count Of Degrees","Closeness Centrality")
	draw(G, pos,centrality, 'CLoseness Centrality')

def katz_centrality(G,pos):
	centrality = nx.katz_centrality(G)
	unique_degrees = list(sorted(set(centrality)))
	plot(centrality,"Unique Degrees","Count Of Degrees","Katz Centrality")
	draw(G, pos,centrality, 'Katz Centrality')

def page_rank(G,pos):
	centrality=nx.pagerank(G)
	unique_degrees = list(sorted(set(centrality)))
	plot(centrality,"Unique Degrees","Count Of Degrees","Page Rank")
	draw(G, pos,centrality, 'Page Rank')

def local_clustering(G,pos):
	centrality = nx.clustering(G)
	unique_degrees = list(sorted(set(centrality)))
	plot(centrality,"Unique Degrees","Count Of Degrees","Local Clustering")
	draw(G,pos,centrality, 'Local Clustering')

def values(G):
	centrality = nx.average_clustering(G)
	print(centrality)
	transitivity = nx.transitivity(G)
	print(transitivity)

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

	pos = nx.spring_layout(G)
	print(nx.info(G))
	nx.draw(G)
	plt.show()
	degree_centrality(G,pos)
	normalized_degree_centrality(G,pos)
	eigenvector_centrality(G,pos)
	betweenness_centrality(G,pos)
	closeness_centrality(G,pos)
	katz_centrality(G,pos)
	page_rank(G,pos)
	local_clustering(G,pos)
	values(G)
