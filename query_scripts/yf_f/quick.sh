 echo ****************************doing KBAL ;
while [[ ! -f KBAL.yfq.csv ]]
do ./curl.sh KBAL > .yfq.csv ; 
cat .yfq.csv; 
done; 
