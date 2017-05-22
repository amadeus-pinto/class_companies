rm run_all.sh
rm *.csv

while IFS='' read -r line || [[ -n "$line" ]]; do
echo "Text read from file: $line"
p=`echo $line | awk -F ',' '{print $1}'`
echo  " echo ****************************doing $p ;
while [[ ! -f $p.yfq.csv ]]
do ./curl.sh $p > $p.yfq.csv ; 
cat $p.yfq.csv; 
done; "  >> run_all.sh
done < ../../data/urls.csv 

chmod a+rwx run_all.sh
echo wrote run_all.sh
head run_all.sh
