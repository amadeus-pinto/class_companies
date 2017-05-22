tic=$1 ; 
a=`html2text "https://finance.yahoo.com/quote/$tic" | grep '^# '  | perl -pi -e 's/# //g' | perl -pi -e 's/,//g'`; echo $tic,$a
