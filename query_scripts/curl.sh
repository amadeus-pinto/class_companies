tic=$1
curl -f "https://finance.yahoo.com/quote/$tic/profile?p=$tic" | sed 's/Description</\n\n\nDescription\</g' | grep 'Description<'  | awk -F '</p></section>' '{print $1}' | awk -F '">' '{print $2}'
