 echo ****************************doing KBAL ;
while [[ ! -f KBAL.yfq.csv ]]
do ./curl.sh KBAL > KBAL.yfq.csv ; 
cat KBAL.yfq.csv; 
done; 
