import http
from collections import namedtuple

class Article(namedtuple('Article', 'title html url')):

    def isFetched(self):
        return self.html

    def fetchFromUrl(self):
        conn = http.client.HTTPSConnection(self.url)
        conn.request("GET", "/")
        r1 = conn.getresponse()
        assert r1.status == 200, "wrong status: " + str(r1.status)
        self.html = r1.read()

