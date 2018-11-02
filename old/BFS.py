#Adj[u] = {v in V | (u,v) in E}
# Adj = [{a: [c]}, b:[c,a], c:[b]]
def BFS():
	level = {s:0}
	parent = {s: None}
	i = 1
	frontier = [s] # level i-1
	while frontier:
		next = [] #level i
		for u in frontier:
			for v in Adj[u]:
				if v not in level:
					level[v] = i
					parent[v] = u
					next.append(v)
		frontier = next
		i += 1

'''
 Depth-first-search(DFS)
 recursively explore graph, backtracking as necessary
'''
def DFSVisit(v,Adj,s):
	for v in Adj[s]:
		if v not in parent:
			parent[v] = s
			DFSVisit(v,Adj,v)

def DFS(v, Adj):
	parent = {}
	for s in v:
		if s not in parent:
			parent[s]= None
			DFSVisit(v,Adj,s)
'''
sigle shortest paths problem-Dijkstra and Bellman Ford
General structure (no negative cycles)
Initialize for u in V, d[v]= infinity, parent[u] = NIL
d[s] = 0
repeat 
	select edge(u,v) (somehow)
		if d[v] > d[u]+w(u,v)
			d[v] = d[u]+w(u,v)
			parent[v] = u
	until all edges have d[v] <= d[u]+w(u,v)

Lemma: the relaxation operation maintains the invarant
proof: by induction on the number of steps, 
by indcition d[u] >= delta(s,u), 
by the triangel inequelity, delta(s,v) <= delta(v,u) + delta(s,u)
delta(s,v) <= d[u] + w(u,v) = d[v]

DAGs can not have -ve cycles O(V+E) time
1) topological sort the DAG, path from u to v imply that u is befor v in the ordering
2) one pass over vertices in topologically sorted orders relaxy each edge that levels each vertices

'''
def Dijstra(G,W,s):
	Initialize(G,s), S = None, Q = V[G]
	while Q != None:
		u = EXTRACT-MIN(Q)
		S = S or {u}
		for each vertex v in Adj[u]
		relax(u,v,w)


def BellmanFord(G,W,source):
	Initialize for v in V, S = None, Q = V[G]
	for l = 1 to |V|-1
		for each edge(u,v) in G
			relax(u,v,w)
	for each edge(u,v) in G
		if d[v] > d[u] + w(u,v)
			then report -ve cycle exists

'''
Theorem: if G = (V,E) contains no -ve weight cycles, then after B_Fexcutes, d[v] = delta(s,v) for all v in V
Corollary: if a value d[v] false to converge after |V|-1 passes, there exists a -ve weight cycle reachable from s
'''

peak finding problem
def peakfinding(nums, sta):
	if a[n/2] < a[n/2-1] then only look at left half 1 to n/2-1 to look for a peak
	else if a[n/2] < a[n/2+1] then look from n/2+1 to n 
	else n/2 position is peak

