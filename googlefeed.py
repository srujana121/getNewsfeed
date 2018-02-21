import feedparser
import re
import urllib2
from bs4 import BeautifulSoup
import urllib2
from feedbuilder import feedbuilder
from redirected import getredirectedurl
from cleanhtml import cleanhtmltags

def parse_description(summary):
    soup = BeautifulSoup(summary, 'html.parser')
    des= soup.find_all("font", {"size": "-1"})[1]
    des_string=unicode.join(u'\n',map(unicode,des))
    return  des_string

def getgooglerss(query , num=10):
    query_list = query.split(' ')
    query_format = query_list[0]
    for i , q in enumerate(query_list):
        if (i>0):
            query_format=query_format+'+'+q
    url = "http://news.google.com/news?q="+query_format+"&output=rss"+"&num="+str(num)
    parsed = feedparser.parse(url)
    return url , parsed

class googlefeed(feedbuilder):
    def getdescription(self):
        parseddescription = parse_description((self.ent).summary)
        cleaneddecription = cleanhtmltags(parseddescription)
        return cleaneddecription
    def getpubagency(self):
        summary = self.ent.summary
        soup = BeautifulSoup(summary, 'html.parser')
        try:
            pub_agency= soup.find_all("font", {"size": "-1"})[0]
            ch1 = pub_agency.findChildren()
            pub_agency = ch1[1].string
        except:
            pub_agency = None
        return pub_agency
    def getimageurl(self):
        summary=self.ent.summary
        soup = BeautifulSoup(summary, 'html.parser')
        try:
            return soup.find("img").attrs['src']
        except:
            return None
