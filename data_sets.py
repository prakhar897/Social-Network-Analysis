import networkx as nx
import matplotlib.pyplot as plt

all_degrees = []
normalized_degrees = []

def degree_centrality(G):
	global all_degrees
	all_degrees = [val for (node, val) in G.degree()]
	#print(all_degrees)
	unique_degrees = list(sorted(set(all_degrees))) #all unique degrees

	count_of_degrees = []

	for i in unique_degrees:
		x = all_degrees.count(i)
		count_of_degrees.append(x)

	plt.title("Degree_centrality")
	plt.xlabel("Unique Degrees")
	plt.ylabel("Count Of Degrees")
	plt.plot(unique_degrees,count_of_degrees)
	plt.show()

def normalized_degree_centrality(G):
	global normalized_degrees
	n = len(all_degrees)
	v = 1/(n-1)
	for i in range(0,n):
		normalized_degrees.append(v*all_degrees[i])
	#print(normalized_degree)

	unique_degrees = list(sorted(set(normalized_degrees))) #all unique degrees

	count_of_degrees = []

	for i in unique_degrees:
		x = normalized_degrees.count(i)
		count_of_degrees.append(x)
	#print(unique_degrees)
	#print(count_of_degrees)

	plt.title("Normalized Degree centrality")
	plt.xlabel("Unique Degrees")
	plt.ylabel("Count Of Degrees")
	plt.plot(unique_degrees,count_of_degrees)
	plt.show()

def eigenvector_centrality(G):
	centrality = nx.eigenvector_centrality(G)
	print(centrality)



def main():
	G = nx.read_edgelist('ego-twitter/out.ego-twitter')
	print(nx.info(G))
	nx.draw(G)
	plt.show()
	degree_centrality(G)
	normalized_degree_centrality(G)
	eigenvector_centrality(G)
if __name__ == "__main__": 
    main()