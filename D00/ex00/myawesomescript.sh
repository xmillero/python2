curl $1 2>&1 | grep 'http' | cut -d '"' -f2
