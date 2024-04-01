import scrapy
from game_try.items import GameTryItem

class YouxiSpider(scrapy.Spider):
    name = 'youxi'  # 该名字非常关键, 我们在启动该爬虫的时候需要这个名字
    allowed_domains = ['4399.com']  # 爬虫抓取的域.
    start_urls = ['http://www.4399.com/flash/']  # 起始页

    def parse(self, response, **kwargs):
        # response.text  # 页面源代码
        # response.xpath()  # 通过xpath方式提取
        # response.css()  # 通过css方式提取
        # response.json() # 提取json数据

        # 用我们最熟悉的方式: xpath提取游戏名称, 游戏类别, 发布时间等信息
        li_list = response.xpath("//ul[@class='n-game cf']/li")
        for li in li_list:
            name = li.xpath("./a/b/text()").extract_first()
            category = li.xpath("./em/a/text()").extract_first()
            date = li.xpath("./em/text()").extract_first()

            # dic = {
            #     "name": name,
            #     "category": category,
            #     "date": date
            # }太low了
            item = GameTryItem()
            item["name"] = name
            item["category"] = category
            item["date"] = date
            yield item

            # 将提取到的数据提交到管道内.
            # 注意, 这里只能返回 request对象, 字典, item数据, or None
