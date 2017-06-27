import numpy as np
import sys,os 
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from sklearn import linear_model
import random

#kmeans


def get_intragroup(sdf=None):
	l=[]
	b=sdf.mean(axis=1)
	sdf['mean']=b
	for symbol in sdf.columns:
		if symbol=='mean':
                    print 'continuing!!!'
                    continue
	        est=linear_model.LinearRegression(copy_X=True,fit_intercept=True)
		ssdf = sdf[[symbol,'mean']].dropna(how='any',axis=0)
	        y= ssdf[symbol].values.tolist()
	        x= ssdf['mean'].values.reshape(-1, 1)
		try:
			est.fit(x,y)
		except:
			print '!!!!!!!!nan!', symbol
			continue
		r2= est.score(x,y)
		a= est.coef_[0]
		b=est.intercept_
		myl=[symbol,r2,a,b]
		l.append(myl)

	gdf = pd.DataFrame(l,columns=['symbol','r2','a','b'])
        print 'intra-group:\n', gdf.mean()
        return gdf

def get_extragroup(sdf=None,other=None):
    l=[]
    sdf['mean']=  other
    for symbol in sdf.columns:
	if symbol=='mean':continue
        est=linear_model.LinearRegression(copy_X=True,fit_intercept=True)
	ssdf = sdf[[symbol,'mean']].dropna(how='any',axis=0)
	y= ssdf[symbol].values.tolist()
	x= ssdf['mean'].values.reshape(-1, 1)
	try:
		est.fit(x,y)
	except:
		print '!!!!!!!!nan!', symbol
		continue
	r2= est.score(x,y)
	a= est.coef_[0]
	b=est.intercept_
	myl=[symbol,r2,a,b]
	l.append(myl)
    gdf = pd.DataFrame(l,columns=['symbol','r2','a','b'])
    print 'extra-group:\n',gdf.mean()
    return gdf
        
def get_target(df=None, cname=None,ncl=None):
    c=df.copy()
    if cname=='random':
        cname = 'random.'+str(ncl).zfill(3)
        c[cname] = [random.randint(1,ncl) for X in range(len(c))]
    elif cname=='gics':
	mycol = [X for X in c.columns if 'gics' in X][0]
        nd={11:2,24:4,68:6,157:8}
        if ncl in nd.keys():
            cname = 'gics.'+str(ncl).zfill(3)
	    c[cname] = c[mycol].astype(str).apply(lambda x: x[0:nd[ncl]])
        else:
            print 'gics not here... out' ; sys.exit()
    elif cname=='text':
        cname = [X for X in c.columns if 'text' in X][0]
    elif cname=='fact':
        cname = [X for X in c.columns if 'fact_' in X][0]


    c=c[['symbol',cname]]
    return c,cname

def get_w_mu_sig(values=None,weights=None):
    """
    Return the weighted average and standard deviation.

    values, weights -- Numpy ndarrays with the same shape.
    """
    mu  = np.average(values, weights=weights)
    var = np.average((values-mu)**2, weights=weights)  # Fast and numerically precise
    return mu,np.sqrt(var) 


def get_w_fits(indf=None,wrstr=None):
        
	indf['w']=indf['n']/indf['n'].sum()
	ws=np.sum(indf['n']/indf['n'].sum()*indf['r2'])
	indf.sort('n',inplace=True,ascending=False)
        indf=indf.loc[indf.n>1]
        b= get_w_mu_sig(values=indf.r2.values.tolist(),weights=indf.w.values.tolist())
        l = pd.DataFrame([[wrstr,b[0],b[1]]])#,columns=['type','mu','sigma'])
        l.columns  = ['type','mu','sigma']
        print 'WRITING THESE!'
        print '**\n', l
        print '**\n',wrstr, b
        print '**\n',indf
        indf.to_csv('./class_csvs/'+wrstr+'.csv',index=False)
        l.to_csv(   './class_csvs/'+'s.'+wrstr+'.csv',index=False)
        return b

if __name__ == '__main__':

        try:	
		ncl = int(sys.argv[1])
        except Exception:
		ncl = 11 
        
        try:	
		ctype = str(sys.argv[2])
        except Exception:
                ctype='kmeans'

        try:	
		cname = str(sys.argv[3])
        except Exception:
		cname = 'gics' 
        try: 
                var = str(sys.argv[4])
        except Exception:
                var = '1d.AVERAGE'


        strncl=str(ncl).zfill(3)
	cpath='../data/'+ctype+'.'+strncl+'.csv'
        print '------------------------'
	print 'n=',ncl
        print 'cl=',ctype
	print 'type=',cname
        print '------------------------'


	path='./../data/'+var+'.csv'
	A = pd.read_csv('../data/'+var+'.csv',index_col='#TIMESTAMP')
	c = pd.read_csv(cpath)	

        c,cname=get_target(df=c,cname=cname,ncl=ncl)

	Al=[]
        Bl=[]
	for cluster in c[cname].unique():
                print 'cluster={}'.format(cluster)
		names= c.loc[c[cname]==cluster].symbol.values.tolist()
		acols = list(set(A.columns.values.tolist()) & set(names))
                bcols = list(set(A.columns.values.tolist()) - set(names))
		Al.append(A[acols])
                Bl.append(A[bcols])
        #Al are group-wise

	gl,el=[],[]
	for X,Y in zip(Al,Bl):
            print 'advance group... '
            gl.append(get_intragroup(sdf=X))
            el.append(get_extragroup(sdf=X,other=Y.mean(axis=1))) 

	gw,ew=[],[]

	for X in gl: gw.append([len(X), X.r2.mean()])
	for Y in el: ew.append([len(Y), Y.r2.mean()])
        
	wgdf= pd.DataFrame(gw,columns=['n','r2'])
	egdf= pd.DataFrame(ew,columns=['n','r2'])

        b=get_w_fits(indf=wgdf,wrstr=var+'.'+cname+'.i')
        d=get_w_fits(indf=egdf,wrstr=var+'.'+cname+'.e')


	#wgdf.plot(kind='scatter',x='w',y='r2',title=cname+' w v.r2')
	#plt.tight_layout()
	#plt.savefig('plot.'+cname+'.pdf')
	#plt.clf()

	#wgdf['r2'].plot(kind='hist',title=cname+'r2')
	#plt.tight_layout()
	#plt.savefig('hist.'+cname+'.pdf')
	#plt.clf()
  


	

