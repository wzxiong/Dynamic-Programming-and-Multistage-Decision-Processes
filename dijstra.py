# Dijkstra's algorithm for shortest paths
# David Eppstein, UC Irvine, 4 April 2002

# import efficient store method
from priodict import priorityDictionary
def Dijkstra(G,start,end=None):
	"""
      Dijkstra method, G is dictionary represent node chart
      start and end is starting point and end point
	"""
	D, P = {}, {} # dictionary of final distances predecessors
	Q = priorityDictionary()  # estimate dist
	Q[start] = 0
	for v in Q:
		D[v] = Q[v]
		if v == end: break	
		for w in G[v]:
			vwLength = D[v] + G[v][w]
			if w in D:
				if vwLength < D[w]:
					raise ValueError
     #"Dijkstra: found better path to already-final vertex"
			elif w not in Q or vwLength < Q[w]:
				Q[w] = vwLength
				P[w] = v
	return (D,P)
def shortestPath(G,start,end):    
    """
    Find a single shortest path from the given start vertex
    to the given end vertex.
    The input has the same as Dijkstra().
    The output is a list of distrance and shortest path
    """
    D,P = Dijkstra(G,start,end)
    Path = [] 
    while 1:
        Path.append(end)
        if end == start:
           break
        end = P[end]
    Path.reverse()
    return D,Path
G = {'1':{'2':5, '3':1},
     '2':{'3':4, '4':6},
     '3':{'4':7, '5':2},
     '4':{'6':2},
     '5':{'6':8, '4':3}}
#G={'1':{'2':1,'3':1,'4':1},
#   '2':{'1':1,'3':1,'5':1,'4':0.5},
#   '3':{'4':2,'1':1,'2':1,'5':0.5},
#   '4':{'1':1,'3':2,'5':2,'2':0.5},
#   '5':{'2':1,'3':0.5,'4':2}}
print shortestPath(G,'1','6')