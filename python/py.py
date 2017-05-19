import os
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from collections import Counter
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

#kmeans
articles_df = pd.read_pickle("./data/articles.pkl")
print articles_df.head()
print articles_df.describe()
print articles_df.info()
vectorizer = TfidfVectorizer(stop_words='english',max_features=200)
X = vectorizer.fit_transform(articles_df['content'])
features = vectorizer.get_feature_names()
kmeans = KMeans()
kmeans.fit(X)

#print "cluster centers:"
#print kmeans.cluster_centers_

top_centroids = kmeans.cluster_centers_.argsort()[:,-1:-11:-1]
print top_centroids
print "top features for each cluster:"
for num, centroid in enumerate(top_centroids):
	print "cluster={},top features={}".format( num, ", ".join(features[i] for i in centroid) )
	    
#random headlines from cluster
assigned_cluster = kmeans.transform(X).argmin(axis=1)
for i in range(kmeans.n_clusters):
	cluster = np.arange(0, X.shape[0])[assigned_cluster==i]
	sample_articles = np.random.choice(cluster, 3, replace=False)
	print "cluster {}:".format( i )
	for article in sample_articles:
		print "    %s" % articles_df.ix[article]['headline']
