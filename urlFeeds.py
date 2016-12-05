from article import *
import json

def extractUrlsFromJsonRss(rssJson):
    items = json.loads(rssJson)['feedEntries']

    #print(items)

    return [Article(title=i['title'], url=i['url'], html="") for i in items]
