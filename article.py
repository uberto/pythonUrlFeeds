from urllib.request import urlopen
from collections import namedtuple

class Article(namedtuple('Article', 'title html url')):

    def isFetched(self):
        return self.html

    def fetchArticleFromUrl(self):

        r = urlopen(self.url)
        assert r.status == 200, "Error fetching url " + self.url + " " + str(r.status)
        htmlBody = r.read().decode("utf-8")
        return Article(title=self.title, url=self.url, html=htmlBody)
        

