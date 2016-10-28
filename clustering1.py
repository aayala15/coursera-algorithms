# What is the maximum spacing of a 4-clustering?
import itertools
from collections import Counter, defaultdict

def MakeSet(x):
	x.parent = x
	x.rank   = 0

def Union(x, y):
	xRoot = Find(x)
	yRoot = Find(y)
	if xRoot.rank > yRoot.rank:
		yRoot.parent = xRoot
	elif xRoot.rank < yRoot.rank:
		xRoot.parent = yRoot
	elif xRoot != yRoot:
		yRoot.parent = xRoot
		xRoot.rank = xRoot.rank + 1

def Find(x):
	if x.parent == x:
		return x
	else:
		x.parent = Find(x.parent)
		return x.parent

class Node:
	def __init__ (self, label):
		self.label = label
	def __str__(self):
		return self.label

def kclusters(graph, k):
	clusters = [Node(str(x)) for x in range(number_of_nodes)]
	[MakeSet(node) for node in clusters]
	for w in sorted(graph, key=graph.get):
		sets =  set([str(Find(x)) for x in clusters])
		if len(sets) <= k:
			break
		else:
			if Find(clusters[w[0]]) != Find(clusters[w[1]]):
				Union(clusters[w[0]], clusters[w[1]])
	return(clusters)

def max_spacing(graph, clusters):
	distance = float("inf")
	for w in graph:
		if Find(clusters[w[0]]) != Find(clusters[w[1]]):
			if graph[w] < distance:
				distance = graph[w]
	return(distance)


print("LOAD THE DATA")
graph = defaultdict(int)
with open('clustering1.txt', 'r') as f:
	data = str.split(f.readline())
	number_of_nodes = int(data[0])
	for line in f:
		data = [int(a) for a in str.split(line)]
		graph[(data[0]-1,data[1]-1)] = data[2]

clusters = kclusters(graph, 4)
sets = set([str(Find(x)) for x in clusters])
print(sets)

print(max_spacing(graph, clusters))