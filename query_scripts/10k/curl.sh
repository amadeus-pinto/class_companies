tic=$1

echo '--------------------------DOING ' $tic
mya=`curl -f "https://www.sec.gov/cgi-bin/browse-edgar?CIK=$tic&owner=exclude&action=getcompany" | grep -m1 -A 1 '10-K' |  perl -pi -e 's/"/  /g'  | awk '{print $6}' | sed '/^$/d'` ; echo 'got url' ; myb=`echo "https://www.sec.gov$mya"`;  myc=`curl -f $myb  | grep -m 2 -A1 '10-K'  | grep 'href'   | awk -F '"' '{print $4}'` ; b=`echo "https://www.sec.gov$myc"`; echo $b; echo 'querying... '  ; 
html2text $b > temp ; echo 'done...' ;  cat temp | sed  '/^$/d' | sed '/^  $/d'  > $tic.10k.txt ; rm temp  ; echo 'wrote it;'  ; head $tic.10k.txt  ; echo 'now  compressing...' ; gzip $tic.10k.txt ; echo 'done' 
