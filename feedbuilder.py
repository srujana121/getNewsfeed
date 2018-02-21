import feedparser
import re
import urllib2
from bs4 import BeautifulSoup
import urllib2
from redirected import getredirectedurl

class feedbuilder(object):
    def __init__(self,ent):
        self.ent=ent
        dval = None
        self.attributes = dict.fromkeys(['title','imageurl','description','pubdate','pubagency','originalurl','cleanurl'],dval)
    def gettitle(self):
        return self.ent.title if 'title' in self.ent else None
    def getimageurl(self):
        return self.ent.news_image if 'news_image' in self.ent else None
    def getdescription(self):
        return self.ent.summary if 'summary' in self.ent else None
    def getpubdate(self):
        return self.ent.published_parsed if 'published_parsed' in self.ent else None
    def getpubagency(self):
        return self.ent.news_source if 'news_source' in self.ent else None
    def getoriginalurl(self):
        return self.ent.link if 'link' in self.ent else None
    def getcleanurl(self):
        return getredirectedurl(self.getoriginalurl())
    def filldict(self):
        self.attributes['title']=self.gettitle()
        self.attributes['imageurl']=self.getimageurl()
        self.attributes['description']=self.getdescription()
        self.attributes['pubdate']=self.getpubdate()
        self.attributes['pubagency']=self.getpubagency()
        self.attributes['originalurl']=self.getoriginalurl()
        self.attributes['cleanurl']=self.getcleanurl()
    def printdict(self):
        for it in self.attributes:
            print
            print it , self.attributes[it]
