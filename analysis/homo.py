import numpy as np
import sys,os 
import pandas as pd
import glob
from collections import Counter
import matplotlib.pyplot as plt
import random
#params = {'legend.fontsize': 10,'legend.loc':'best'}
#plt.rcParams.update(params)


if __name__ == '__main__':

    gpath='../python/class_csvs/s.*.csv'
    gfi=glob.glob(gpath)
    
    l=[]
    for g in gfi:
        print g
        l.append(pd.read_csv(g))
    A=  pd.concat(l)
    A['type']=A['type'].str.replace('.','_')
    A['n'] = A['type'].apply(lambda x: int(x.split('_')[-2]))
    A['g'] = A['type'].apply(lambda x: x.split('_')[-1])
    A['t'] = A['type'].apply(lambda x: x.split('_')[0::-2][0])
    A['g.t'] =  A['g'].apply(lambda x: 'extra' if x=='e' else 'intra') +'@'+A['t']
    A.drop('type',1,inplace=True)
    print A

    

    groups = A.groupby('g.t')
    fig, ax = plt.subplots()
    ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling
    for name, group in groups:
        print name
        if 'extra' in name: marker='x'
        else: marker='o'
        #ax.errorbar(group['n'], group['mu'],yerr=0.25*group['sigma'], fmt='-o',label=name,marker=marker, linestyle='-', ms=12)
        ax.plot(group['n'], group['mu'],label=name,marker=marker, linestyle='-', ms=12)

    plt.xlabel('n_clusters')
    plt.ylabel('<R**2>')

    ax.legend()
    plt.savefig('r2.v.n.price.pdf')

    print 'wrote fig'
