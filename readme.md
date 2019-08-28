Sign up for https://www.blinkist.com

Read a random note
```
find . -type d \( -name .git -o -name blinks_daily \) -prune -o \( -name "*.mkd" -o -name "*.md" \) |shuf -n 1
```

Read a random downloaded daily blink
```
find blinks_daily -type f | shuf -n 1
```

Grab quotes from a book and add to quotes.md
```
grep -E "\`.*\`" BOOK |sed "s/$/ -- BOOK /" |sed "s/\`//g" |sed "s/^/> /" >> quotes.mkd
```

