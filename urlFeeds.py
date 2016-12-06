import json
import sys

from article import *
from workers import *
from persistence import *
from httpFetcher import *

def extractUrlsFromJsonRss(rssJson):
    items = json.loads(rssJson)['feedEntries']

    #print(items)

    return [Article(title=i['title'], url=i['url'], html="", tags=[]) for i in items]


def processAndSaveAll(db, articles):

    funs = [fetch, tag123, tag4]
    
    processed = processAll(funs, articles )
    map(db.saveArticle, processed )

def fetch(a):
    print("fetching %s" % a.title)
    return a.fetchArticleFromUrl()

def tag123(a):
    print("tagging 123 %s" % a.title)
    return a.tagArticle('t1', 't2', 't3')

def tag4(a):
    print("taggging 4 %s" % a.title)
    return a.tagArticle('t4')


if __name__ == '__main__':
    if (len(sys.argv) != 2):
        raise EnvironmentError("Please specify the url from where to download the rss list")
    rssJson = downloadFromUrl(sys.argv[1])
    articles = extractUrlsFromJsonRss(rssJson)    
    db = Persistence('urlFeedDb.json')
    processAndSaveAll(db, articles)

