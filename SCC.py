from collections import Counter, defaultdict
import sys
import resource

sys.setrecursionlimit(10 ** 6)
resource.setrlimit(resource.RLIMIT_STACK, (2 ** 25, 2 ** 25))

def DFSLoop(graph, rg):
	global s
	for vertex in rg:
		if vertex not in visited:
			s = vertex
			DFS(graph, vertex)

def DFS(graph, start):
	global t
	visited.add(start)
	leader[start] = s
	for vertex in graph[start]:
		if vertex not in visited:
			DFS(graph, vertex)
	t += 1
	time[start] = t

print("LOAD THE DATA")
G = defaultdict(set)
Grev = defaultdict(set)
with open('SCC.txt', 'r') as f:
	for line in f:
		g = [int(i) for i in str.split(line)]
		G[g[0]].add(g[1])
		Grev[g[1]].add(g[0])

print("STEP 1")
visited = set()
leader = defaultdict(int)
time = defaultdict(int)
t = 0
s = None
DFSLoop(Grev, sorted(Grev.keys(), reverse=True))

print("STEP 2")
visited = set()
leader = defaultdict(int)
DFSLoop(G, sorted(time.keys(), key=time.get, reverse=True))

print(Counter(leader.values()))
