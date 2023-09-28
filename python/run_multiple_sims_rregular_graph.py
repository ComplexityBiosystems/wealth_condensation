import numpy as np
import sdeint
import scipy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LogNorm
import networkx as nx
import wealth_condensation as wc
import pickle

## define parameters
N=160
m=0.5
s=1
mu=0.1
sigma=1
phi=0.
f=0.
sigmat=0.
c=4
N_real=100
J0s=[0.01,0.05,0.1,0.2,0.5,1,2,5]
t_tot=30
dt=.01
n_step=int(t_tot/dt)
df1=pd.DataFrame(columns=["i_real","J0","N","m","s","n_step","result"])
G=nx.random_regular_graph(c,N)
A0=nx.to_numpy_array(G)

for i_real in range(N_real):        
    for J0 in J0s:
        A,B=wc.simulate.interaction_matrix(N,mu,sigmat,m,phi,f,J0,A0,sigma,s,c)
        ## initial conditions
        x=np.ones(N+1)
        result=wc.simulate.integrate_sde(x,A,B,t_tot,dt)
        result=result[int(2*n_step/3):,:]
        df0 = pd.DataFrame({"i_real":[i_real],"J0":[J0],
                            "N":[N],"m":[m],"s":[s],"n_step":[n_step],"result": [result]})
        df1=pd.concat([df1,df0])

df1.to_pickle("../data/rg_resultsN160c4.p.gz")