# I installed pyperclip and pyshorteners packages for this project

import pyshorteners

url = input("Enter your long url: ")

def shortenurl(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))

shortenurl(url)
