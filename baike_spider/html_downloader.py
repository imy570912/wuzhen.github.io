# coding=utf8
import urllib2

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        reponse = urllib2.urlopen(url)

        if reponse.getcode() != 200: #表示请求失败
            return None

        return reponse.read()
