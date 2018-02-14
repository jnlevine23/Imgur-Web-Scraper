#! python3
#Imgur scraping Program
#opens result links to various images after performing a search on Imgur
import requests
import sys
import webbrowser
from bs4 import BeautifulSoup
import pprint

#command line - script will read specific searches based on command line input
print('Searching through Imgur...') #display text
#get imgur search URL by relevance filter
#join with search criteria from command line
res = requests.get('https://imgur.com/search/relevance?q=' + ' '.join(sys.argv[1:]))
print(res) #error checking

#BeautifulSoup to parse through HTML
imgurSoup = BeautifulSoup(res.text, 'html.parser')
#search for all <a> elements that contain an href attribute
resultLinks = []
for a in imgurSoup.find_all('a', href=True):
    resultLinks.append(a['href'])

#New list with only links that contain 'gallery'
resultLinksCleaned = [result for result in resultLinks if '/gallery/' in result]

#pprint.pprint(resultLinksCleaned)

#webbrowser to pull up results in new tabs
#for search results that return less than 5 results
num = min(5, len(resultLinksCleaned))
#display desired images in new browser tabs
for i in range(num):
    webbrowser.open('https://imgur.com' + resultLinksCleaned[i])
