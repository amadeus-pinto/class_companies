tic=$1; 
curl "http://www.marketwatch.com/investing/stock/$tic" | grep -A 10 'p class="description__text' | sed '/span class="descr/,$d' | sed '/<p /d' | perl -pi -e 's/^            //g'  | sed '/^$/d'  | perl -pi -e 's/&#xD;&#xA;//g'  
