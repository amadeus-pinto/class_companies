tic=$1 ; curl "http://www.nasdaq.com/symbol/$tic" | grep 'FIS_BUSINESS' | awk -F '#' '{print $1}' | awk -F 'href="' '{print $2}'
#curl -f $a | sed '/^</d'  | sed '/^	\$/d' | sed '/^	&/d'  > $tic.sec.txt 
#wc -l $tic.sec.txt

#tic='cznc' ; st=`curl "http://www.nasdaq.com/symbol/$tic" | grep -A 5 'Company Description (as filed with'` ;  echo $st ; grep \"$st\" cznc.sec.txt
