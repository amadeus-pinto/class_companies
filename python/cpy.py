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
def get_source(sourcestr=None,rewrite=False):
	if sourcestr==None: print 'sourcestring undefined!' ; sys.exit()

	if rewrite:
		fil = glob.glob('../data/'+sourcestr+'_data/*.txt')
		l=[]
		for ind,f in enumerate(fil):
			symb = f.split('/')[-1].split('.')[0]
			if os.stat(f).st_size == 0: 
				print '***** symbol {} empty; '.format(symb); continue
			data = pd.read_csv(f,sep=' ', header = None)
			data=data.values.tolist()[0]
			datal = " ".join(str(X) for X in data)
			l.append([symb,datal])
			print 'i={},symbol={},len={}'.format(ind, symb,len(data))
		articles_df =pd.DataFrame(l,columns=['symbol','content'])
		articles_df.to_csv('../data/'+sourcestr+'_data.csv',index=False)
		return articles_df
	else:
		print 'reading ../data/'+sourcestr+'_data.csv'
		b=  pd.read_csv('../data/'+sourcestr+'_data.csv')
		print b.info(verbose=True,null_counts=True)
		return b


if __name__ == '__main__':
	
	
	dosvd=False
	#http://scikit-learn.org/stable/auto_examples/text/document_clustering.html#sphx-glr-auto-examples-text-document-clustering-py


	#mw =get_source(sourcestr='mw',rewrite=True)
	#sys.exit()

	dfl=[]
	articles_df = pd.DataFrame()
	slist = ['yf','gf','mw']
	for source in slist:
		sdf  = get_source(sourcestr=source, rewrite=False) 
		sdf.rename(columns={'content':source+'content'},inplace=True)
		dfl.append(sdf)
	for df in dfl:
		if articles_df.empty:

			articles_df = df
		else:
			articles_df  = pd.merge(articles_df,df,on='symbol',how='outer')

	#articles_df = pd.merge(gf_df,yf_df,on='symbol',how='outer')
	ccols = [X for X in articles_df.columns if 'content' in X ]
	n=pd.DataFrame(); 
	for c in ccols: 
		n[c] = articles_df[c].apply(lambda x: len(str(x).split(' ')))


	print articles_df.info(verbose=True,null_counts=True)
	articles_df.fillna(' ',inplace=True); 
	mcc =   articles_df.iloc[:,1:].apply(lambda x:  ' '.join(x),axis=1); 
	for c in ccols: articles_df.drop(c,1,inplace=True)
	articles_df['content'] = mcc
	print articles_df.info(verbose=True)
	print articles_df['content'].head()


	#n['all'] = articles_df['content'].apply(lambda x: len(x.split()))
	#n.plot(kind='hist',bins=100,xlim=(0,500))
	#plt.savefig('hist.counts.png')
	#sys.exit()

	vectorizer = TfidfVectorizer(stop_words='english',max_features=None)
	X = vectorizer.fit_transform(articles_df['content'])

	if dosvd:
		svd = TruncatedSVD(n_components=10)
		normalizer = Normalizer(copy=False)
		lsa = make_pipeline(svd, normalizer)
		X = lsa.fit_transform(X)
		explained_variance = svd.explained_variance_ratio_.sum()
		print("Explained variance of the SVD step: {}%".format( int(explained_variance * 100)))

	features = vectorizer.get_feature_names()
	kmeans = KMeans(n_clusters=14)
	#KMeans(n_clusters=8, init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=1, algorithm='auto')
	kmeans.fit(X)
	
	print "cluster centers:"
	print kmeans.cluster_centers_
	
	top_centroids = kmeans.cluster_centers_.argsort()[:,-1:-20:-1]
	print top_centroids
	print "top features for each cluster:"
	for num, centroid in enumerate(top_centroids):
		print "cluster={},top features={}".format( num, ", ".join(features[i] for i in centroid) )
		    
	#random companies  from cluster
	assigned_cluster = kmeans.transform(X).argmin(axis=1)
	for i in range(kmeans.n_clusters):
		cluster = np.arange(0, X.shape[0])[assigned_cluster==i]
		sample_articles = np.random.choice(cluster, 10, replace=False)
		print "cluster {}:".format( i )
		for article in sample_articles:
			print "    %s" % articles_df.ix[article]['symbol']
