Sign up for https://www.blinkist.com

Read a random note
```
find . -type d \( -name .git -o -name blinkist-daily \) -prune -o \( -name "*.mkd" -o -name "*.md" \) |shuf -n 1
```

Read a random downloaded daily blink
```
find . -type f | shuf -n 1
```

Grab quotes from a book and add to quotes.md
```
BOOK="yourbook" && grep -E "\`.*\`" $BOOK |sed "s/$/ -- $BOOK /" |sed "s/\`//g" |sed "s/^/> /" >> ~/notes/quotes.md
```

```
MAILTO=""
0 */6 * * * cd $HOME/code/arafatm/blinkist && /Users/amohamed/homebrew/bin/python3 /Users/amohamed/code/arafatm/blinkist/blinkist_daily_scraper.py >> /Users/amohamed/tmp/cron.log 2>&1
```
