import networkx as nx
import matplotlib.pyplot as plt

all_degrees = []
normalized_degrees = []

def plot(list_values,xlabel,ylabel,title):
	unique_degrees = list(sorted(set(list_values))) #all unique degrees

	count_of_degrees = []

	for i in unique_degrees:
		x = all_degrees.count(i)
		count_of_degrees.append(x)

	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.plot(unique_degrees,count_of_degrees)
	plt.show()

def degree_centrality(G):
	global all_degrees
	all_degrees = [val for (node, val) in G.degree()]
	plot(all_degrees,"Unique Degrees","Count Of Degrees","Degree_centrality")

def normalized_degree_centrality(G):
	global normalized_degrees
	n = len(all_degrees)
	v = 1/(n-1)
	for i in range(0,n):
		normalized_degrees.append(v*all_degrees[i])
	plot(all_degrees,"Unique Degrees","Count Of Degrees","Normalized Degree_centrality")

def eigenvector_centrality(G):
	centrality = nx.eigenvector_centrality(G).values()
	#print(centrality)
	unique_degrees = list(sorted(set(centrality)))
	print(unique_degrees)
	plot(centrality,"Unique Degrees","Count Of Degrees","EigenVector Centrality")



def main():
	G = nx.read_edgelist('ego-twitter/out.ego-twitter')
	#print(nx.info(G))
	#nx.draw(G)
	#plt.show()
	degree_centrality(G)
	normalized_degree_centrality(G)
	eigenvector_centrality(G)
if __name__ == "__main__": 
    main()