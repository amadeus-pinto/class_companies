echo ****************************doing ARTNA ;
while [[ ! -f ARTNA.10k.txt.gz ]]
do
	./curl.sh ARTNA  
done;  

