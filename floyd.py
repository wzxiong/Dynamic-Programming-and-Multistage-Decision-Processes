# -*- coding: utf-8 -*-
def floydwarshall(graph):
    pred = {}
    for u in graph:
        dist[u] = {}
        pred[u] = {}
        for v in graph:
            dist[u][v] = float('inf')
            pred[u][v] = 'None'
        dist[u][u] = 0
        for neighbor in graph[u]:
            dist[u][neighbor] = graph[u][neighbor]
            pred[u][neighbor] = u

    for t in graph:
        # given dist u to v, check if path u - t - v is shorter
        for u in graph:
            for v in graph:
                newdist = dist[u][t] + dist[t][v]
                if newdist < dist[u][v]:
                    dist[u][v] = newdist
                    pred[u][v] = pred[t][v] # route new path through t
    return dist, pred
 
 
 
graph = {'1':{'2':1,'3':2},
         '2':{'1':1,'3':4,'4':3,'5':9},
         '3':{'1':2,'2':4,'4':8,'5':-5},
         '4':{'2':-2,'3':8,'5':7,'6':5},
         '5':{'3':6, '2':9,'4':7,'6':3},
         '6':{'5':3,'4':5}}
#dist, pred = floydwarshall(graph)
#def PATH(u,v):
#    path = [u]
#    while u!=v:
#        u=pred[u][v]
#        path.append(u)
#    return path
#print PATH('1','6')
#print 'Predecesors in shortest path:'
#for v in pred:
#    print  v, pred[v]
#print 'Shortest distance from each vertex:'
#for v in dist:
#    print  v, dist[v]
G={'1':{'2':1,'3':1,'4':1},
   '2':{'1':1,'3':1,'5':1,'4':0.5},
   '3':{'4':2,'1':1,'2':1,'5':0.5},
   '4':{'1':1,'3':2,'5':2,'2':0.5},
   '5':{'2':1,'3':0.5,'4':2}}
dist, pred = floydwarshall(G)
print 'Shortest distance from each vertex:'
for v in dist:
    print  v, dist[v]