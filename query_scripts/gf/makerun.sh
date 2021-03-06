rm run_all.sh
rm *.txt

while IFS='' read -r line || [[ -n "$line" ]]; do
echo "Text read from file: $line"
p=`echo $line | awk -F ',' '{print $1}'`
echo  "
echo ****************************doing $p ;
while [[ ! -f $p.gf.txt ]]
do
./curl.sh $p > $p.gf.txt ; 
done; cat $p.gf.txt ; sleep 0.5 ; "  >> run_all.sh
done < ../../data/urls.csv 

chmod a+rwx run_all.sh
echo wrote run_all.sh
head run_all.sh > quick.sh
chmod a+rwx quick.sh
echo 'wrote quick.sh'
cat quick.sh
