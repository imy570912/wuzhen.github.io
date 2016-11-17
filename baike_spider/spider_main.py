# coding=utf8
from baike_spider import html_downloader
from baike_spider import html_outputer
from baike_spider import html_parser
from baike_spider import url_manager


class SpiderMain(object):
    # 初始化所有的组件
    def __init__(self):
        self.urls = url_manager.UrlManager() # 初始化url管理器
        self.downloader = html_downloader.HtmlDownloader() # html下载器
        self.parser = html_parser.HtmlParser() # html解析器
        self.outputer = html_outputer.HtmlOutputer() # html输出器

    # 爬虫总调度程序
    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url) # url总人口
        # 当url管理器中有带爬取的url的时候，则继续获取待爬去的url
        while self.urls.has_new_url():
            try: # 碰到死链会爬取不到，异常处理爬取不到的页面
                new_url = self.urls.get_new_url()
                print 'carw %d: %s' % (count,new_url)
                #启动下载器来下载这个url并存放在html_cont中
                html_cont = self.downloader.download(new_url)
                #使用解析器来解析下载下来的网页，获取新的url和新的数据
                new_urls, new_data = self.parser.parse(new_url,html_cont)
                print '获取到新的url为: %s' % new_urls
                #将新的url添加进url管理器中，  将数据添加进输出器中
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                # 爬取到1000个就不爬取
                if count == 1000:
                    break

                count = count + 1
            except:
                print 'craw failed'

        #将输出器中的数据输出到一个网页
        self.outputer.output_html()



if __name__ == "__main__":
    root_url = "http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%C3%C0%C5%AE&ala=1&fr=ala&alatpl=cover&pos=0#z=0&pn=&ic=0&st=-1&face=0&s=0&lm=-1"

    obj_spider = SpiderMain()
    obj_spider.craw(root_url)