# -*- coding: utf-8 -*-
def bellman_ford(graph, start):
    dist, pred = dict(), dict()
    for u in graph:
        dist[u], pred[u] = float('inf'), None
    dist[start] = 0
    for _ in range(len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                # find lower distance
                if dist[v] > dist[u] + graph[u][v]:
                    dist[v], pred[v] = dist[u] + graph[u][v], u
    for node in graph:
        for neigh in graph[node]:
            assert dist[neigh] <= dist[node] + graph[node][neigh], "Negative weight cycle."
    return dist, pred
    
if __name__ == '__main__':
    graph = {'1':{'2':1,'3':2},
             '2':{'1':1,'3':4,'4':3,'5':9},
             '3':{'1':2,'2':4,'4':8,'5':-5},
             '4':{'2':-2,'3':8,'5':7,'6':5},
             '5':{'3':6, '2':9,'4':7,'6':3},
             '6':{'5':3,'4':5}}
    for i in graph.keys():
        distance, predecessor = bellman_ford(graph, start=i)
        #print sorted([(i,)+item for item in distance.items()])
        print i,sorted(distance.items())
        #print i,sorted(predecessor.items())
        
#    F={'1':{'2':1,'3':1,'4':1},
#   '2':{'1':1,'3':1,'5':1,'4':0.5},
#   '3':{'4':2,'1':1,'2':1,'5':0.5},
#   '4':{'1':1,'3':2,'5':2,'2':0.5},
#   '5':{'2':1,'3':0.5,'4':2}}
#    for i in F.keys():
#        distance, predecessor = bellman_ford(F, start=i)
#        #print sorted([(i,)+item for item in distance.items()])
#        print i,sorted(distance.items())
#        #print i,sorted(predecessor.items())