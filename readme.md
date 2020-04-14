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

# Setup

make sure to set up deploykey in repo
```
sudo apt install python3-pip
pip3 install bs4 html5lib tomd

python3 blinkist_daily_scraper.py # to test
```

`crontab -e # and copy text below`
```
MAILTO=""
0 */6 * * * cd $HOME/code/arafatm/blinkist && python3 $HOME/code/arafatm/blinkist/blinkist_daily_scraper.py >> $HOME/tmp/cron.log 2>&1
```
