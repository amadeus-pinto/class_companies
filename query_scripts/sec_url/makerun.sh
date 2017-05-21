rm run_all.sh
rm *.txt

while IFS='' read -r line || [[ -n "$line" ]]; do
echo "Text read from file: $line"
p=`echo $line | awk -F ',' '{print $1}'`
d=`echo $line | awk -F ',' '{print $1}'  | tr '[:upper:]' '[:lower:]'`
echo  "
echo ****************************doing $p ;
./curl.sh \"$d\" >  $p.sec_url.txt ; 
cat $p.sec_url.txt ;   sleep 0.5 "  >> run_all.sh
done < ../../data/urls.csv 

chmod a+rwx run_all.sh
echo wrote run_all.sh
head run_all.sh
