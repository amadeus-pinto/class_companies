
echo ****************************doing tic ;
while [[ ! -f tic.gf.txt ]]
do
./curl.sh tic > tic.gf.txt ; 
done; cat tic.gf.txt ; sleep 0.5 ; 

