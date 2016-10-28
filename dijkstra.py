from collections import Counter, defaultdict

def dijkstra(path, dist, start, target):
	explored = set()
	shortest = {key: 0 for key in graph_path.keys()}
	
	explored.add(start)
	shortest[start] = 0
	while target not in explored:
		minimum = float('inf')
		for v in explored:
			for i, w in enumerate(path[v]):
				if w not in explored:
					d = shortest[v] + dist[v][i]
					if d < minimum:
						wstar = w
						dstar = d
						minimum = d
		explored.add(wstar)
		shortest[wstar] = dstar
	return(shortest[target])


print("LOAD THE DATA")
graph_path = defaultdict(list)
graph_dist = defaultdict(list)
with open('dijkstraData.txt', 'r') as f:
# with open('dijkstraTest.txt', 'r') as f:
	for line in f:
		data = str.split(line)
		s = int(data.pop(0))
		graph_path[s] = [int(str.split(d, ',')[0]) for d in data]
		graph_dist[s] = [int(str.split(d, ',')[1]) for d in data]

targets = [7,37,59,82,99,115,133,165,188,197]
# targets = [5]
result = [dijkstra(graph_path,graph_dist, 1, t) for t in targets]

print(result)
