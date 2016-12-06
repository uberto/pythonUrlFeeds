from collections import namedtuple
from httpFetcher import *

class Article(namedtuple('Article', 'title html url tags')):

    def isFetched(self):
        return self.html

    def fetchArticleFromUrl(self):
        htmlBody =downloadFromUrl(self.url)
        return Article(title=self.title, url=self.url, html=htmlBody, tags=[])


    def tagArticle(self, *newTags):
        return Article(title=self.title, url=self.url, html=self.html, tags=newTags)
