import unittest

import urlFeeds

def fun(x):
    return x + 1

  

class MyTest(unittest.TestCase):
 
    def testSuccess(self):
        self.assertEqual(fun(3), 4)

    def testProcessUrlLists(self):
        rssExample = """someResult = {
    'feedEntries': [{
    url: "www.arkera.ai/article/1",
    title: "Article 1, The Story of Arkera’s Beginnings",
    imageUrl: "www.arkera.ai/article/image/1"
    }, {
    url: "www.arkera.ai/article/2",
    title: "Article 2, The Story of Arkera’s Beginnings 2",
    imageUrl: "www.arkera.ai/article/image/2"
    }]
}"""   

        urls = urlFeeds.extractUrlsFromRss(rssExample)
        self.assertEqual(len(urls), 2)



if __name__ == '__main__':
    unittest.main()