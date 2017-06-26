import numpy as np
import sys,os 
import pandas as pd
import glob
from collections import Counter
import matplotlib.pyplot as plt
import random
import seaborn as sns

pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 1000)
sns.set(context="paper", font="monospace")

if __name__ == '__main__':

    try:
    	nclu=int(sys.argv[1])
    except:
    	nclu=8
    print '********doing n_clusters=',nclu


    strnclu=str(nclu).zfill(3)
    fi='kmeans.'+strnclu
    nd={11:2,24:4,68:6,157:8}
    gpath='../data/'+fi+'.csv'
    c = pd.read_csv(gpath)
    col = [x for x in c.columns if 'gics' in x][0]
    mycol = [x for x in c.columns if 'text' in x][0]

    cname = 'gics.'+str(nclu).zfill(3)
    c[cname] = c[col].astype(str).apply(lambda x: x[0:nd[nclu]])
    c.drop(col,1,inplace=True)


    o = pd.read_csv('../data/company_bio.csv')
    c = pd.merge(c,o,how='left')
    
    groups=c.groupby(cname)
    mgroups=c.groupby(mycol)
    q=[]
    for group in c[mycol].unique():
        gdf =  c.loc[c[mycol]==group][['symbol','name','mc']]
        gdf.sort('mc',ascending=False,inplace=True)
        names = ",".join(gdf[0:10].name.values.tolist())
        q.append( [group,names])
    q=pd.DataFrame(q)
    q.columns=[mycol,'names']
    q.names = q['names'].apply(lambda x: x.lower())
    print q


    textvals=groups[mycol].value_counts()
    li=[]
    for l in textvals.index.levels[0]:
        print l
        li.append([l, textvals[l].sort_index()])

    
    B= pd.concat([x[1] for x in li] ,axis=1)
    B.columns = [x[0] for x in li]
    B= B.fillna(0).astype(int)
    P=100*B/B.sum(axis=0)
    P=P.round(0)
    sns.heatmap(P, annot=True ,annot_kws={"size": 12})
    plt.xlabel("gics")
    plt.savefig('p.'+fi+'.pdf')
    plt.clf()
    sns.heatmap(B, annot=True  ,annot_kws={"size": 12})
    plt.xlabel("gics")
    plt.savefig('b.'+fi+'.pdf')
    gicscounts=groups[mycol].count()
    mycounts=mgroups[cname].count()


    print gicscounts.sort_values()
    print mycounts.sort_values()
    mycounts = pd.DataFrame(mycounts)
    mycounts.columns= ['n']
    F= pd.concat([mycounts,q[['names']]],axis=1)
    print F
    for i,X in enumerate(F.names.values):
        print i,': ',X


