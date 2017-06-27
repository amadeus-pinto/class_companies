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
from sklearn.cluster import AgglomerativeClustering
from text_cluster import get_adf
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition

pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def do_kmeans(X=None,n_clusters=None,df=None,features=None):
	kmeans = KMeans(n_clusters=n_clusters)
	kmeans.fit(X)
	
	assigned_cluster = kmeans.transform(X).argmin(axis=1)
        print 'kmean*******class dist:',Counter(assigned_cluster)

	df['kmeans.fact_'+str(n_clusters).zfill(3)] = assigned_cluster
	#top_centroids = kmeans.cluster_centers_.argsort()[:,-1:-10:-1]
        top_centroids = kmeans.cluster_centers_.argsort(axis=-1)[:,-1:-10:-1]

	cl = []
	for num, centroid in enumerate(top_centroids):
		cl.append([ num,  [", ".join(features[i] for i in centroid) ]])
		    
	l=pd.DataFrame(cl)
	l.columns=['kmeans.fact_'+str(n_clusters).zfill(3),'features']
	df = pd.merge(l,df)
	print 'n,inertia',n_clusters,kmeans.inertia_
        writecols = ['symbol','gics8','kmeans.fact_'+str(n_clusters).zfill(3)]
	df[writecols].to_csv('../data/kmeans.fact.'+str(n_clusters).zfill(3)+'.csv',index=False)
	for i in range(kmeans.n_clusters):
		cluster = np.arange(0, X.shape[0])[assigned_cluster==i]
		#print cluster
		ss = df.loc[df['kmeans.fact_'+str(n_clusters).zfill(3)]==i]
		ss.sort('mc',ascending=False,inplace=True)
		print "cluster {}:".format( i )
		print ss[['name','mc','gics8']][0:10]
		print ss.iloc[0][['features']].values.tolist()
	#print df.info(verbose=True,null_counts=True)
        #print df.head()
        #b = df.rename(columns={'kmeans.fact_'+str(n_clusters).zfill(3):'label'})#,inplace=True)
        #return b[['label','name']] 


def do_hiercl(X=None,n_clusters=None,df=None,features=None):
    connectivity='ward'
    model = AgglomerativeClustering(linkage='ward',connectivity=None,n_clusters=n_clusters)

    assigned_cluster = model.fit_predict(X.values)
    print 'hc_'+connectivity+'*******class dist:',Counter(assigned_cluster)
    
    df['hier.fact_'+str(n_clusters).zfill(3)] = assigned_cluster

    writecols = ['symbol','gics8','hier.fact_'+str(n_clusters).zfill(3)]
    df[writecols].to_csv('../data/hier.fact.'+str(n_clusters).zfill(3)+'.csv',index=False)
    for i in df['hier.fact_'+str(n_clusters).zfill(3)].unique(): 
    	cluster = np.arange(0, X.shape[0])[assigned_cluster==i]
    	ss = df.loc[df['hier.fact_'+str(n_clusters).zfill(3)]==i]
    	ss.sort('mc',ascending=False,inplace=True)
    	print "cluster {}:".format( i )
    	print ss[['name','mc','gics8']][0:10]
    	print ss.iloc[0][['features']].values.tolist()
    print df.info(verbose=True,null_counts=True)

def get_factor_df(q='q0'):
    qpath = '../data/fa_data/'+q+'.csv'
    print 'getting quarter={} from {}'.format(q,qpath)
    df = pd.read_csv(qpath,header=0)#,dtype={'gics8':np.int32})
    df['gics8'] = df.gics8.fillna(0).astype(int)
    df.rename(columns={'mktval':'mc'},inplace=True)
    return df

if __name__ == '__main__':
	
	try:
		n_clusters=int(sys.argv[1])
	except:
		n_clusters=8
	print 'doing n_clusters=',n_clusters

        df =  get_factor_df(q='q0')
        df.dropna(thresh=30,inplace=True)
        df.fillna(0,inplace=True)


        rdq =  [x for x in df.columns if 'xrdq2' in x]
        for r in rdq:
            df[r].fillna(0,inplace=True)

        #df.dropna(how='any',inplace=True)
        #
        #remove if any null - 685 left
        #30                ~ 1600
        #25
        #20
        #15
        #10
        print df.info(verbose=True,null_counts=True)




        
        objl = [key for key in dict(df.dtypes) if dict(df.dtypes)[key] in ['object', 'string']]
        ancdrl = ['mc','gics8','fyr_used']

        dropl = objl+ancdrl
        X = df.copy()


        for d in dropl:
            X.drop(d,1,inplace=True)
        X.fillna(0,inplace=True)

        print X.info(verbose=True,null_counts=True)
        features = X.columns.values.tolist()
        do_kmeans(X=X,n_clusters=n_clusters,df=df,features=features)
        do_hiercl(X=X,n_clusters=n_clusters,df=df,features=features)


        '''
        n_components=3
        pca = decomposition.PCA(n_components=n_components)
        pca.fit(X)
        pcX = pca.transform(X)
        pcX = pd.DataFrame(X,columns=['pc_'+str(y).zfill(2) for y in range(n_components) ])
        print lidf.columns
        print pcX.columns
        print len(lidf)
        print len(pcX)
        print type(lidf)
        print type(pcX)
        sys.exit()
        pcX = pd.concat([lidf,pcX],axis=1)
        print pcX
        sys.exit()
        y=pcX.label
        print y
        sys.exit()
    
        mylabels = [('cl_'+str(x),x) for x in pcX.label.unique()]


        fig = plt.figure(1, figsize=(4, 3))
        plt.clf()
        ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

        for name, label in mylabels:
            ax.text3D(X[y == label, 0].mean(),
              pcX[y == label, 1].mean() + 1.5,
              pcX[y == label, 2].mean(), name,
              horizontalalignment='center',
              bbox=dict(alpha=.5, edgecolor='w', facecolor='w'))
        # Reorder the labels to have colors matching the cluster results
        y = np.choose(y, [1, 2, 0]).astype(np.float)
        ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap=plt.cm.spectral)

        ax.w_xaxis.set_ticklabels([])
        ax.w_yaxis.set_ticklabels([])
        ax.w_zaxis.set_ticklabels([])

        plt.show()

        '''
