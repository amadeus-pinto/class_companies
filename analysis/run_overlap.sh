

rm summary.*.pdf
ipython overlap.py 11 'kmeans_fact' > kmeans.fact.011.out  
ipython overlap.py 11 'kmeans_text' > kmeans.text.011.out  
ipython overlap.py 11 'hier_fact'   > hier.fact.011.out 
ipython overlap.py 11 'hier_text'   > hier.text.011.out 
pdfunite p.*011*.pdf summary.p.011.pdf 

ipython overlap.py 24 'kmeans_fact' > kmeans.fact.024.out  
ipython overlap.py 24 'kmeans_text' > kmeans.text.024.out  
ipython overlap.py 24 'hier_fact'   >   hier.fact.024.out 
ipython overlap.py 24 'hier_text'   >   hier.text.024.out 
pdfunite p.*024*.pdf summary.p.024.pdf 




ipython overlap.py 68 'kmeans_fact' > kmeans.fact.068.out  
ipython overlap.py 68 'kmeans_text' > kmeans.text.068.out  
ipython overlap.py 68 'hier_fact'   >   hier.fact.068.out 
ipython overlap.py 68 'hier_text'   >   hier.text.068.out 
pdfunite p.*068*.pdf summary.p.068.pdf 




ipython overlap.py 157 'kmeans_fact' > kmeans.fact.157.out  
ipython overlap.py 157 'kmeans_text' > kmeans.text.157.out  
ipython overlap.py 157 'hier_fact'   >   hier.fact.157.out 
ipython overlap.py 157 'hier_text'   >   hier.text.157.out 
pdfunite p.*157*.pdf summary.p.157.pdf 

rm p.*.pdf
