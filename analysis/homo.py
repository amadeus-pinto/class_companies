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

    try:	
    	var = str(sys.argv[1])
    except Exception:
    	var = '1d.RETURN' 


    gpath='../python/class_csvs/s.'+var+'*.csv'
    gfi=glob.glob(gpath)
    
    l=[]
    for g in gfi:
        print 'doing', g
        l.append(pd.read_csv(g))
    print 'concating... '
    A=  pd.concat(l)
    print 'done'
    A['type']=A['type'].str.replace('.','_')
    A['n'] = A['type'].apply(lambda x: int(x.split('_')[-2]))
    A['g'] = A['type'].apply(lambda x: x.split('_')[-1])

    print A.type
    A['t'] = A['type'].str.replace('_fact','.fact')
    A['t'] = A['t'].   str.replace   ('_text','.text')

    A['t'] = A['t'].apply(lambda x: ".".join(x.split('_')[0:3]))
    A['g.t'] =  A['g'].apply(lambda x: 'extra' if x=='e' else 'intra') +'@'+A['t']
    A.drop('type',1,inplace=True)

    print A['g.t']
    groups = A.groupby('g.t')
    fig, ax = plt.subplots()
    ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling
    for name, group in groups:
        if 'extra' in name: 
            marker='x'
        elif 'intra' in name: 
            marker='o'
        #ax.errorbar(group['n'], group['mu'],yerr=0.25*group['sigma'], fmt='-o',label=name,marker=marker, linestyle='-', ms=12)
        ax.plot(group['n'], group['mu'],label=name,marker=marker,linestyle='--',ms=12)
        print name
        print group[['n','mu']]

    plt.xlabel('n_clusters')
    plt.ylabel('<R**2>')
    plt.legend(loc='best',prop={'size':6})


    wrstr = 'r2.v.n.'+var+'.pdf'
    plt.savefig(wrstr)

    print 'wrote fig', wrstr
