import urllib2
def getredirectedurl(url):
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor)
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    try:
        op = opener.open(url)
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        op = opener.open(url)
        return op.geturl()
    except:
        print "Error in getting final url"
        return url
