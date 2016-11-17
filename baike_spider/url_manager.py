# coding=utf8
#url管理器
class UrlManager(object):

    #构造方法初始化
    def __init__(self):
        self.new_urls = set() #新的url列表
        self.old_urls = set() #爬取过的url列表

    #向utl管理器中添加一个url
    def add_new_url(self, url):
        if url is None: #如果url为空则直接返回
            return
        #如果当前url既不在新url列表，也不在旧的url列表中，则表示这个url是一个全新的url
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url) #将这个全新的url放入新url列表


    # 向url管理器中批量添加url
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls: #如果urls不为空的话，就循环调用add_new_url方法添加到new_urls列表中
            self.add_new_url(url)

    #判断管理器中是否有新的url
    def has_new_url(self):
        return len(self.new_urls) != 0

    #从url管理器中获取一个新的url
    def get_new_url(self):
        new_url = self.new_urls.pop()#pop方法从列表中移除一个元素，并返回这个元素
        #再将这个url添加进old_urls中
        self.old_urls.add(new_url)
        return new_url
