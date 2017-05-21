


tic=$1 ; a=`curl "http://www.nasdaq.com/symbol/$tic" | grep 'FIS_BUSINESS' | awk -F '#' '{print $1}' | awk -F 'href="' '{print $2}'`
echo $a
curl -f $a | sed '/^</d'  | sed '/^	\$/d' | sed '/^	&/d'  > $tic.nas.txt 
wc -l $tic.nas.txt

