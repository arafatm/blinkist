import requests
import urllib.parse
from bs4 import BeautifulSoup
import urllib3
from html import unescape
import tomd
import os
import pathlib
import re
import argparse

# Parse Args
parser = argparse.ArgumentParser()
parser.add_argument("username", help="Blinkist username")
parser.add_argument("password", help="Blinkist password")
#parser.add_argument("book", help="Book url")
#parser.add_argument("books", help="Comma delimited list of Blinkist book URLs", type=lambda s: [str(item) for item in s.split(',')])

# extract args
args = parser.parse_args()

# Read username & password
username = args.username
password = args.password
#books = [re.sub("https://www.blinkist.com/en/nc/reader/", "", elem) for elem in args.books]

#print("{0} : {1} : {2}".format(username, password, book_url))
#print("scraping: "+ str(books))

# Session and headers
session = requests.session()
session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3021.0 Safari/537.36'
session.headers['origin'] = 'https://www.blinkist.com'
session.headers['upgrade-insecure-requests'] = "1"
session.headers['content-type'] = "application/x-www-form-urlencoded"
session.headers['accept-encoding'] = "gzip, deflate, br"
session.headers['authority'] = "www.blinkist.com"

# Get CSRF token
login_url="https://www.blinkist.com/en/nc/login"
response = session.get(url=login_url)
soup = BeautifulSoup(response.content.decode('utf-8'), "html5lib")
csrf_token = soup.find("meta", {"name": "csrf-token"}).attrs["content"]
print("csrf_token: " + csrf_token)

# Login
response = session.post(url=login_url, data={
    "login[email]": username,
    "login[password]": password,
    "login[facebook_access_token]": None,
    "utf8": unescape("%E2%9C%93"),
    "authenticity_token": csrf_token
}, allow_redirects=True)

response = session.get(url="https://www.blinkist.com/en/nc/library/")
soup = BeautifulSoup(response.content.decode('utf-8'), "html5lib")
soup = soup.find("div", {"class": "libraryV2__section--active libraryV2__section__reading"})
booklib = soup.find_all("a", {"class": "book-card__main-link"})
#" data-book-path="/en/books/the-easy-way-to-stop-smoking-en" data-reader-path="/en/nc/reader/the-easy-way-to-stop-smoking-en" href="/en/nc/reader/the-easy-way-to-stop-smoking-en"></a>

books = []
for book in booklib:
    book = book.attrs["data-book-path"]
    book = re.sub("/en/books/", "", book)
    books.append(book)
    print("\t",book)

# Scrape books
for bookname in books:

    bookurl="https://www.blinkist.com/books/"+bookname

    book = session.get(url=bookurl)
    book = BeautifulSoup(book.content.decode('utf-8'), "html5lib")
    book = book.find("div", {"class": "book__header-container"})
    title = book.find("h1", {"class": "book__header__title"}).string.strip()
    author = book.find("div", {"class": "book__header__author"}).string.strip()
    img = book.find("img")["src"]

    print("title: " + title)
    print("author: " + author)
    #print("\ttitle: {0} by {1}".format(title, author))

    bookfile = re.sub(" ", ".", title) + "." + re.sub(" ", ".", author) + ".md"
    if pathlib.Path("blinkist-new/" + bookfile).exists():
        print("- file exists in blinks_new: " + bookfile)
        continue

    if pathlib.Path("blinks/" + bookfile).exists():
        print("- file exists in blinks: " + bookfile)
        continue

    bookfile = "blinkist-new/" + bookfile
    bookurl="https://www.blinkist.com/en/nc/reader/"+bookname
    book = session.get(url=bookurl)
    book = BeautifulSoup(book.content.decode('utf-8'), "html5lib")
    content = str(book.find("article", {
        "class": "shared__reader__blink reader__container__content"}).
        contents).strip()
    content = tomd.convert(content)
    content = re.sub('#', '##', content)
    booktext = "# " + title + "\n"
    booktext = booktext + "*" + author + "*\n\n" 
    booktext = booktext +  "Source: [Blinkist: " + title + "]"
    booktext = booktext + "(" + bookurl + ")" + "\n\n"
    booktext = booktext + "![" + title + "](" + img + ")\n\n"
    booktext = booktext + content + "\n\n"

    with open(bookfile, "w", encoding="utf8") as text_file:
        text_file.write(booktext)
    print("- added " + bookfile)

# print(book)
