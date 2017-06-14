# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 19:48:04 2017

@author: xiong
"""

import numpy as np
from scipy.stats import gamma
q = np.array([-1]*500).reshape(5,100)
qnew = np.array([-2]*500).reshape(5,100)
tr = np.linspace(0,4.,100)
u = np.zeros(500).reshape(5,100)
u[-1,:]=1
l=4./99
G={'1':{'2':1,'3':1,'4':1},
   '2':{'1':1,'3':1,'5':1,'4':0.5},
   '3':{'4':2,'1':1,'2':1,'5':0.5},
   '4':{'1':1,'3':2,'5':2,'2':0.5},
   '5':{'2':1,'3':0.5,'4':2}}
unew = np.array([0.]*500).reshape(5,100)
unew[-1,:],unew[2,0]=1,-1
#record iteration time
n=0
#check converge
while np.max(abs(unew-u))>0.1:
    #set up new iterate matrix
    if n!=0:
        u=unew.copy()
        q=qnew.copy()
    n=n+1
    for node in range(1,len(G)):
        for t in range(len(tr)):
            for neigh in G[str(node)]:
                #calculate reliability for each road
                if str(node) in ['1','2'] and neigh in ['1','2']:
                    r=sum([gamma.pdf(tr[time]-l/2,1,scale=1)*l*u[int(neigh)-1][t-time] for time in range(t+1)])
                elif str(node) in ['1','3'] and neigh in ['1','3']:
                    r=sum([gamma.pdf(tr[time]-l/2,2,scale=0.5)*l*u[int(neigh)-1][t-time] for time in range(t+1)])
                elif str(node) in ['1','4'] and neigh in ['1','4']:
                    r=sum([gamma.pdf(tr[time]-l/2,2,scale=0.5)*l*u[int(neigh)-1][t-time] for time in range(t+1)])
                elif str(node) in ['2','3'] and neigh in ['2','3']:
                    r=sum([gamma.pdf(tr[time]-l/2,2,scale=0.5)*l*u[int(neigh)-1][t-time] for time in range(t+1)])
                elif str(node) in ['2','4'] and neigh in ['4','2']:
                    r=sum([gamma.pdf(tr[time]-l/2,1,scale=0.5)*l*u[int(neigh)-1][t-time] for time in range(t+1)])
                elif str(node) in ['2','5'] and neigh in ['5','2']:
                    r=sum([gamma.pdf(tr[time]-l/2,1,scale=1)*l*u[int(neigh)-1][t-time] for time in range(t+1)])
                elif str(node) in ['3','4'] and neigh in ['4','3']:
                    r=sum([gamma.pdf(tr[time]-l/2,2,scale=1)*l*u[int(neigh)-1][t-time] for time in range(t+1)])
                elif str(node) in ['3','5'] and neigh in ['3','5']:
                    r=sum([gamma.pdf(tr[time]-l/2,1,scale=0.5)*l*u[int(neigh)-1][t-time] for time in range(t+1)])
                else:
                    r=sum([gamma.pdf(tr[time]-l/2,2,scale=1)*l*u[int(neigh)-1][t-time] for time in range(t+1)])
                #if higher reliability exist, save this valuue
                if r > u[node-1][t]:
                    unew[node-1][t], qnew[node-1][t] = r, neigh

                #else:
                 #   unew[node-1][t],qnew[node-1][t] = u[node-1][t],q[node-1][t]
            #print(unew)
print(unew)
print(qnew)