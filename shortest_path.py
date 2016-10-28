from heapq import heappush, heappop
from collections import defaultdict
import numpy as np

def add_source(nv, graph):
	for v in range(nv):
		graph[0].update({v+1: 0})

def bellman_ford(nv, source, graph):
	dist = {}
	for v in range(nv):
		dist[v] = float("inf")
	dist[source] = 0
	
	for i in range(nv-1):
		for u in graph:
			for v in graph[u]:
				if dist[v] > dist[u] + graph[u][v]:
					dist[v] = dist[u] + graph[u][v]
	
	for u in graph:
		for v in graph[u]:
			if dist[v] > dist[u] + graph[u][v]:
				return([dist, False])
	return([dist, True])

def reweighting(d, graph):
	for u in graph:
		for v in graph[u]:
			graph[u][v] += d[u] - d[v]

def dijkstra(nv, graph, s):
	dist = {}
	Q = []
	
	for v in range(1,nv+1):
		dist[v] = float("inf")
	dist[s] = 0

	heappush(Q, (dist[s], s))
	while Q:
		d, u = heappop(Q)
		if d < dist[u]:
			dist[u] = d
		for v in graph[u]:
			if dist[v] > dist[u] + graph[u][v]:
				dist[v] = dist[u] + graph[u][v]
				heappush(Q, (dist[v], v))
	return dist

def johnson(nv, graph):
	ext_graph = graph.copy()
	rew_graph = graph.copy()
	
	print('STEP1: Bellman Ford')
	add_source(nv, ext_graph)
	[dw, valid] = bellman_ford(nv+1, 0, ext_graph)
	
	dmin = 10000
	if valid:
		print('STEP2: Re-weighting Graph')
		reweighting(dw, rew_graph)
		
		print('STEP3: n-Dijkstra')
		for s in range(1,nv+1):
			dist = dijkstra(nv, rew_graph, s)
			for i in dist:
				dist[i] += dw[i] - dw[s]
			if dmin > min(dist.values()):
				dmin = min(dist.values())
	else:
		dmin = 'Negative cycle'
	return(dmin)

def read_graph(filename):
	graph = defaultdict(dict)
	with open(filename, 'r') as f:
		data = str.split(f.readline())
		nv = int(data[0])
		ne = int(data[1])
		for line in f:
			data = [int(a) for a in str.split(line)]
			graph[data[0]].update({data[1]: data[2]})
	return([nv, ne, graph])


print("LOAD THE DATA")
# [nvtest, netest, gtest] = read_graph('gtest.txt')
[nv1, ne1, g1] = read_graph('g1.txt')
[nv2, ne2, g2] = read_graph('g2.txt')
[nv3, ne3, g3] = read_graph('g3.txt')

# print(johnson(nvtest, gtest))
print(johnson(nv1, g1))
print(johnson(nv2, g2))
print(johnson(nv3, g3))