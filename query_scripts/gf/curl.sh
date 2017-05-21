tic=$1
curl -f "https://www.google.com/finance?q=$tic"  | awk '/companySummary/ && ++n == 1 {getline; print; exit}' 

