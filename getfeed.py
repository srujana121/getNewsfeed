from bingfeed import getbingrss,bingfeed
from googlefeed import getgooglerss,googlefeed

def getparsedfeed(keyword,service = 'bing'):
    feedlist = []
    if service == 'bing':
        url, parsed=getbingrss(keyword)
        for ent in parsed.entries:
            feed = bingfeed(ent)
            feed.filldict()
            feedlist.append(feed.attributes)
    elif service == 'google':
        url, parsed=getgooglerss(keyword)
        for ent in parsed.entries:
            feed = googlefeed(ent)
            feed.filldict()
            feedlist.append(feed.attributes)

    return feedlist
