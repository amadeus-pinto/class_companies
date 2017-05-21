
echo ****************************doing ANCI ;
while [[ ! -f ANCI.sec.txt ]]
do
	./curl.sh anci > ANCI.sec.txt ; 
done; cat ANCI.sec.txt ; 

