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

#kmeans


if __name__ == '__main__':

    gpath='../../onetick/query_1d_script/*.csv'
    myfs = glob.glob(gpath)
    dfl = [None]*len(myfs) 
    for i,g in enumerate(myfs):
        print 'doing------\t', i,g
        try:
            df = pd.read_csv(g)
            #df=df.dropna(how='any',axis=0)
        except:
            print '**not here!'; continue
        try: 
            name=g.split('\\')[-1].split('.csv')[0]
            df = df.loc[np.isfinite(df.AVERAGE)]
            df=df.rename(columns={'AVERAGE':name})
            df['#TIMESTAMP']  = pd.to_datetime(df['#TIMESTAMP'])
            df.sort('#TIMESTAMP',inplace=True)
            df=df[['#TIMESTAMP',name]]
            dfl[i] = df
        except: '**fail' ; continue

    dfl = [x for x in dfl if isinstance(x, pd.DataFrame)]
    dfl = [x.set_index('#TIMESTAMP',inplace=False).reset_index().drop_duplicates(subset='#TIMESTAMP') for x in dfl]
    
    bigdf=pd.DataFrame()
    for X in dfl:
        print 'here',X.columns.values.tolist()
        if bigdf.empty:
            print 'empty'
            bigdf=X
        else:
            bigdf = pd.merge(X,bigdf,on='#TIMESTAMP',how='outer')
    bigdf.sort('#TIMESTAMP',inplace=True)

    bigdf.to_csv('AVERAGE'+'.csv',index=False)
    print bigdf.info(verbose=True,null_counts=True)
    print bigdf.head()
