import numpy as np
import sys,os 
import glob
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from collections import Counter
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer


if __name__ == '__main__':



    
    rootpath='../data/fa_data/'
    #path=rootpath+'Basic_Factors_Cluster_Richie.txt'
    path=rootpath+'Basic_Factor_Cluster_Richie_V2.txt'

    df = pd.read_csv(path,sep='\t',header=0,na_values='NULL')

    print df.head()

    print df.info(verbose=True,null_counts=True)
    #df = df.dropna(how='any',axis=0)
    df['date'] = pd.to_datetime(df.date)
    df['datadate'] = pd.to_datetime(df.datadate)


    gl=['gsector','ggroup','gind','gsubind','fyr_used']
    #for x in gl:
    #    df[x]=df[x].astype(int)
    exl = ['date','iid','cqtr','cusip9','repno','gvkey']
    for x in exl:
        df.drop(x,1,inplace=True)

    df.rename(columns={'gsubind':'gics8','ticker':'symbol','conm':'name'},inplace=True)
    print df.groupby('datadate').count()
    df=df.loc[df.datadate=='2011-06-30']
    df.drop('datadate',1,inplace=True)

    print df.info(verbose=True,null_counts=True)
    print df.head(2)

    print 'factors'
    print pd.Series(df.factor.unique()).sort_values()
    print 'fyr_counts'
    print df.fyr_used.value_counts()
    print 'n_symbols=', len(df.symbol.unique())
    print 'sgms'
    print df.loc[df.symbol=='SGMS']
    print df.info()
    print 'n_symbols=', len(df.symbol.unique())


    ql = [x for x in df.columns if 'q' in x]
    q='q0'

    for q in ql:
        qstr=rootpath+q+'.csv'
        bcols =   ['symbol','fyr_used','factor',q]
        anccols = ['name','symbol','fyr_used','gics8','mktval']
    
        a = pd.pivot_table(df[bcols],values=q, index='symbol',columns = ['factor'])# .reset_index()
        b = df[anccols].drop_duplicates()
        a.reset_index(inplace=True)
        c = pd.merge(a,b,how='left')
        print '*******writing {} len={} to {}'.format(q,len(c), qstr)
        c.to_csv(qstr,index=False)

