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


def get_mc():
        #old hack
        sys.exit()
	mcap = pd.read_csv('../data/mcap.csv')
	t = mcap['mc'].str.split('(\d+)([A-z]+)',expand=True)
	t.columns=['a','b','c','d']
	t['c']=t['c'].map({ 'M':10**6,'B':10**9, 'k':10**3, 'None':10**0})
	t['d'] = t['b'].apply(lambda x: 10**(-len(str(x))))
	t['a']  = pd.to_numeric(t['a'],errors='coerce')
	t['b']  = pd.to_numeric(t['b'],errors='coerce')
	mc = (t.d*t.b+t.a)*t.c
	mcap['mc']=mc
	return mcap

def get_adf():

	#df= pd.read_csv('../data/sname.csv')
        df= pd.read_csv('../data/company_bio.csv')#,dtype={'gics8':np.int})
        df.dropna(axis=0,how='any',inplace=True)
        df['gics8'] = df.gics_subind.astype(int)
	df.drop('gics_subind',1,inplace=True)
        print df.info(verbose=True,null_counts=True)
        return df



def do_kmeans(X=None,n_clusters=None,articles_df=None,features=None):
	kmeans = KMeans(n_clusters=n_clusters,verbose=True)
	kmeans.fit(X)
	
	assigned_cluster = kmeans.transform(X).argmin(axis=1)
        print assigned_cluster
        print 'kmeans_class dist:',Counter(assigned_cluster)

	articles_df['kmeans.text_'+str(n_clusters).zfill(3)] = assigned_cluster
	top_centroids = kmeans.cluster_centers_.argsort()[:,-1:-20:-1]
        print 'top centroids:\n',top_centroids

	cl = []
	for num, centroid in enumerate(top_centroids):
		cl.append([ num,  [", ".join(features[i] for i in centroid) ]])
		    
	l=pd.DataFrame(cl)
	l.columns=['kmeans.text_'+str(n_clusters).zfill(3),'features']
        print l
	articles_df = pd.merge(l,articles_df)
	print 'n,inertia',n_clusters,kmeans.inertia_
        writecols = ['symbol','gics8','kmeans.text_'+str(n_clusters).zfill(3)]
	articles_df[writecols].to_csv('../data/kmeans_text.'+str(n_clusters).zfill(3)+'.csv',index=False)
	for i in range(kmeans.n_clusters):
		cluster = np.arange(0, X.shape[0])[assigned_cluster==i]
		#print cluster
		ss = articles_df.loc[articles_df['kmeans.text_'+str(n_clusters).zfill(3)]==i]
		ss.sort('mc',ascending=False,inplace=True)
		print "cluster {}:".format( i )
		print ss[['name','mc','gics8']][0:10]
		print ss.iloc[0][['features']].values.tolist()
	print articles_df.info(verbose=True,null_counts=True)


def do_hiercl(X=None,n_clusters=None,articles_df=None,features=None):
    connectivity='ward'
    model = AgglomerativeClustering(linkage='ward',connectivity=None,n_clusters=n_clusters)

    X=X.toarray()
    assigned_cluster = model.fit_predict(X)
    #assigned_cluster = model.transform(X).argmin(axis=1)
    print 'hc_class dist:',Counter(assigned_cluster)
    
    articles_df['hier.text_'+str(n_clusters).zfill(3)] = assigned_cluster
    print articles_df
    #top_centroids = kmeans.cluster_centers_.argsort()[:,-1:-20:-1]
    
    # cl = []
    	    
    #l=pd.DataFrame(cl)
    #l.columns=['hier.text_'+str(n_clusters).zfill(3),'features']
    #articles_df = pd.merge(l,articles_df)

    writecols = ['symbol','gics8','hier.text_'+str(n_clusters).zfill(3)]
    articles_df[writecols].to_csv('../data/hier_text.'+str(n_clusters).zfill(3)+'.csv',index=False)
    for i in articles_df['hier.text_'+str(n_clusters).zfill(3)].unique(): 
    	cluster = np.arange(0, X.shape[0])[assigned_cluster==i]
    	ss = articles_df.loc[articles_df['hier.text_'+str(n_clusters).zfill(3)]==i]
    	ss.sort('mc',ascending=False,inplace=True)
    	print "cluster {}:".format( i )
    	print ss[['name','mc','gics8']][0:10]
    	print ss.iloc[0][['features']].values.tolist()
    print articles_df.info(verbose=True,null_counts=True)


if __name__ == '__main__':
	
	
	try:
		n_clusters=int(sys.argv[1])
	except:
		n_clusters=8
	print 'doing n_clusters=',n_clusters

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

	
	articles_df = pd.merge(articles_df,get_adf(),how='inner')
        print 'preview'
        print articles_df.head()

	#n['all'] = articles_df['content'].apply(lambda x: len(x.split()))
	#n.plot(kind='hist',bins=100,xlim=(0,500))
	#plt.savefig('hist.counts.png')
	#sys.exit()

	vectorizer = TfidfVectorizer(stop_words='english',max_features=1000)
	X = vectorizer.fit_transform(articles_df['content'])

	features = vectorizer.get_feature_names()

        do_kmeans(X=X,n_clusters=n_clusters,articles_df=articles_df,features=features)
        do_hiercl(X=X,n_clusters=n_clusters,articles_df=articles_df,features=features)

        print 'done'



