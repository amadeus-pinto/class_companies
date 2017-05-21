echo ****************************doing A ;
while [[ ! -f A.yf.txt ]]
do
	./curl.sh A > A.yf.txt ; 
done; cat A.yf.txt ; 

