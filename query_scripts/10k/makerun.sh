rm run_all.sh
rm *.txt

while IFS='' read -r line || [[ -n "$line" ]]; do
echo "Text read from file: $line"
p=`echo $line | awk -F ',' '{print $1}'`
echo  "
echo ****************************doing $p ;
while [[ ! -f $p.10k.txt.gz ]]
do
./curl.sh $p  
done;  "  >> run_all.sh
done < ../../data/urls.csv 

chmod a+rwx run_all.sh
echo wrote run_all.sh
head run_all.sh
