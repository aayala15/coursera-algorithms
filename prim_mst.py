from collections import Counter, defaultdict

def prim(graph, start):
	explored = set()
	cost = 0
	
	explored.add(start)
	while len(explored) != number_of_nodes:
		minimum = float('inf')
		for v in explored:
			for w in [a[1] for a in graph if a[0]==v]:
				if w not in explored:
					c = graph[(v,w)]
					if c < minimum:
						wstar = w
						minimum = c
			for w in [a[0] for a in graph if a[1]==v]:
				if w not in explored:
					c = graph[(w,v)]
					if c < minimum:
						wstar = w
						minimum = c
		explored.add(wstar)
		cost += minimum
	return(cost)


print("LOAD THE DATA")
graph = defaultdict(int)
with open('edges.txt', 'r') as f:
	data = str.split(f.readline())
	number_of_nodes = int(data[0])
	number_of_edges = int(data[1])
	for i in range(number_of_edges):
		data = [int(a) for a in str.split(f.readline())]
		graph[(data[0],data[1])] = data[2]

# print(graph)
print(prim(graph, 1))
