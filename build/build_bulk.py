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

    try:
        piece = str(sys.argv[1])
    except:
        piece = 'trade_1d'
    wrp = piece.split('_')[1]
    gpath='../../onetick/'+piece+'/*.csv'
    myfs = glob.glob(gpath)
    dfl = [None]*len(myfs) 

    try:
        coln= str(sys.argv[2])
    except:
        coln='AVERAGE'

    print 'coln=',coln

    for i,g in enumerate(myfs):
        if i%500==0:
            print 'doing------\t', i,g
        try:
            df = pd.read_csv(g)
        except:
            print '**not here!'; continue
        try: 
            name=g.split('\\')[-1].split('.csv')[0]
            df = df.loc[np.isfinite(df[coln])]
            df=df.rename(columns={coln:name})
            df['#TIMESTAMP']  = pd.to_datetime(df['#TIMESTAMP'])
            df = df.loc[df['#TIMESTAMP'].dt.dayofweek<=5]
            df.sort('#TIMESTAMP',inplace=True)
            df=df[['#TIMESTAMP',name]]
            dfl[i] = df
        except: '**fail' ; continue

    dfl = [x for x in dfl if isinstance(x, pd.DataFrame)]
    dfl = [x.set_index('#TIMESTAMP',inplace=False).reset_index().drop_duplicates(subset='#TIMESTAMP') for x in dfl]
    
    bigdf=pd.DataFrame()
    for i,X in enumerate(dfl):
        if i%500==0:
            print 'doing------\t', i
        if bigdf.empty:
            bigdf=X
        else:
            bigdf = pd.merge(X,bigdf,on='#TIMESTAMP',how='outer')
    bigdf.sort('#TIMESTAMP',inplace=True)

    finame = '../data/'+wrp+'.'+coln+'.csv'
    print 'writing to csv--- ',finame 
    bigdf.to_csv(finame,index=False)
    print 'finished!'
    print bigdf.info(verbose=True,null_counts=True)
    print bigdf.head()
