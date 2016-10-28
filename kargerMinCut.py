import random, copy

graph = {}
with open('kargerMinCut.txt', 'r') as f:
	for line in f:
		lst = [int(s) for s in line.split()]
		graph[lst[0]] = lst[1:]


def RandomEdge(graph):
	v1 = random.choice(list(graph.keys()))
	v2 = random.choice(list(graph[v1]))
	return v1, v2


def Karger(graph):
	while len(graph) > 2:
		v1, v2 = RandomEdge(graph)
		graph[v1].extend(graph[v2])
		for x in graph[v2]:
			graph[x].remove(v2)
			graph[x].append(v1)
		while v1 in graph[v1]:
			graph[v1].remove(v1)
		del(graph[v2])
	return(len(graph[list(graph.keys())[0]]))


n = 500
i = 0
count = 10000
while i < n:
	data = copy.deepcopy(graph)
	min_cut = Karger(data)
	if min_cut < count:
		count = min_cut
	i += 1
print(count)
