tic=$1
html2text "https://finance.yahoo.com/quote/$tic"  | grep  'Market Cap|' |  perl -pi -e "s/Market Cap\| /$tic,/g" > $tic.yfq.csv ; cat $tic.yfq.csv
