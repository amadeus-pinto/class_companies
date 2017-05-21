rm run_all.sh
rm *.txt

while IFS='' read -r line || [[ -n "$line" ]]; do
echo "Text read from file: $line"
n=`echo $line | awk -F ',' '{print $2}' | perl -pi  -e 's///g'`
p=`echo $line | awk -F ',' '{print $1}'`
echo  "
echo ****************************doing $p ;
while [[ ! -f $p.url.txt ]]
do
curl  $n > $p.url.txt ;
done; cat $p.url.txt ; "  >> run_all.sh
done < ../../data/urls.csv 

chmod a+rwx run_all.sh
echo wrote run_all.sh
head run_all.sh
