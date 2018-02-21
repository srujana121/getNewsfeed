import feedparser
import re
import urllib2
from bs4 import BeautifulSoup
import urllib2
from feedbuilder import feedbuilder
from redirected import getredirectedurl

def getbingrss(query , num=10):
    query_list = query.split(' ')
    query_format = query_list[0]
    for i , q in enumerate(query_list):
        if (i>0):
            query_format=query_format+'+'+q
    url = "https://www.bing.com/news/search?q="+query_format+"&format=RSS"
    parsed = feedparser.parse(url)
    return url , parsed

class bingfeed(feedbuilder):
    pass
