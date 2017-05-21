echo ****doing KBAL ;
while [[ ! -f KBAL.yf.txt ]]
do
./curl.sh KBAL > KBAL.yf.txt ;
done; cat KBAL.yf.txt

