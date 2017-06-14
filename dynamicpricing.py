
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[2]:

#calculate adoption function
def fpq(p,q):
    return (np.exp(-0.1*p))*(0.2+2*q*(np.exp(-2*q)))


# In[65]:

#set up step size
T = 10
Tstep = 0.01
Q = 3
Qstep = 0.01
cost = 4


# In[66]:

#initiate matrix
Profit = np.zeros(300000).reshape(300,1000)
Price = np.zeros(300000).reshape(300,1000)


# In[67]:

#Backward Sweep.:calculate optimal value function and the optimal pricing strategy
for t in range(999,-1,-1):
    for q in range(300):
        if q == 299:
            dq = (Profit[q][t]-Profit[q-1][t])/Qstep
        else:
            dq = (Profit[q+1][t]-Profit[q][t])/Qstep
        Bestprice = 10.0 + cost -dq
        Price[q][t] = Bestprice
        minusdt = (Bestprice - cost + dq)*fpq(Bestprice,q*Qstep)
        Profit[q][t-1] = Profit[q][t]+minusdt*Tstep


# In[68]:

#Forward Sweep: calculate optimal prices and production amounts
PricePath = [Price[11][0]]
Q = [0.1]
FPQ = [fpq(PricePath[0],Q[0])]
for t in range(1,1000):
    quan = (Q[t-1] + Tstep * FPQ[t-1])
    for q in range(299):
        if quan == (q*Qstep):
            optP = (Price[q][t])
            break
        if quan > (q*Qstep) and quan <((q+1)*Qstep):
            ratio = (quan-(q*Qstep))/(Qstep)
            optP = (Price[q][t]+ratio*(Price[q+1][t]-Price[q][t]))
            break           
    PricePath.append(optP) # PricePath is the optimal price from sales 0.11 to the planning horizon(time T=10)
    Q.append(quan) # Q is the adoption amount
    FPQ.append(fpq(optP,quan))#Fpq is adoption rate


# In[69]:

#optimal price
plt.figure(figsize=(10,7))
x = np.linspace(0,10,1000)
plt.plot(x,PricePath)
plt.ylim([0,20])
plt.xlim([0,12])
plt.yticks([0,4,8,12,16])
plt.xlabel('t', fontsize=16)
plt.ylabel('p(t)', fontsize=16)


# In[70]:

#numerical error
plt.figure(figsize=(10,7))
plt.plot(x[1:],FPQ[1:])
plt.xlabel('t', fontsize=16)
plt.ylabel('Adoption rate', fontsize=16)


# In[78]:

#statistic of numeric error 
import pandas as pd
df = pd.DataFrame(FPQ[1:])
df.describe()


# In[79]:

#q distribution
x = np.linspace(0,10,100)
y=[]
for q in x:
    y.append(0.2+2*q*(np.exp(-2*q)))
plt.figure(figsize=(10,7))
plt.plot(x,y)
plt.ylabel('Q(q)', fontsize=16)
plt.xlabel('q', fontsize=16)

