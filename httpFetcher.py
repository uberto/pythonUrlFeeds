from urllib.request import urlopen


def downloadFromUrl(url):
    r = urlopen(url)
    assert r.status == 200, "Error fetching url " + url + " " + str(r.status)
    return r.read().decode("utf-8")

