import scrapy


class UPaSpider(scrapy.Spider):
    name = "u_pa"
    allowed_domains = ["henuucampus.unipus.cn"]
    start_urls = ["https://henuucampus.unipus.cn/"]

    def start_requests(self):

        # 直接从浏览器复制cookie信息
        cookie_str = """
     WithoutLoginDeviceId=02b31e6961054d848ec07600c806a13e; AFsyuFERGolRTTwfegrggT=1589d60ce3f2e154b6e2f84405ca6184; UCANPUS_DNSIP_9679=; __env_tested__Chrome=1700049649996; HWWAFSESID=3024773cf919e3b21f; HWWAFSESTIME=1710919179804; DTS_SESSIONID=71402BE7598F4DCEBE27120C90EDC634; hostUrl="https://henuucampus.unipus.cn"; ucamUserId=05e2127ae5c34fdc80d4118f950a67f7; ucamUserToken=174394534d45127334f3f379183bb413; Hm_lvt_8a1d0cf914523c7ed112dbd25e018957=1709272990,1710157227,1710919181; Hm_lvt_6e6adccba669782ce55df7c210d9563e=1709272990,1710157227,1710919181; Hm_lpvt_6e6adccba669782ce55df7c210d9563e=1710919419; Hm_lpvt_8a1d0cf914523c7ed112dbd25e018957=1710919419; Y1vJ4IdorMglXdNk="zv+EQnrh3bJ2nQwHj/fYkWytQPjrMymXVMNbdH91cyA="; SSOExpireTime=1710926778; jwt=eyJhbGciOiJSUzI1NiIsImtpZCI6InVuaXB1cy1zc28ifQ.eyJqdGkiOiJ5Ylp6Z0c1WGNFaHNSWEl0YzBRdDhRIiwiaWF0IjoxNzEwOTE5NTc4LCJleHAiOjE3MTA5MjY3NzgsIm5iZiI6MTcxMDkxOTUxOCwiaXNzIjoiaHR0cHM6Ly9zc28udW5pcHVzLmNuIiwiYXVkIjoiY24udW5pcHVzLnNzby5qd3QiLCJzdWIiOiIxMDAwMDAwIiwib3BlbklkIjoiMDVlMjEyN2FlNWMzNGZkYzgwZDQxMThmOTUwYTY3ZjciLCJ1c2VybmFtZSI6IjE1NTM3Mjg5NjYwIiwibmlja25hbWUiOiJ5YW5nZnJlZSIsInBob25lIjoiMTU1MzcyODk2NjAiLCJ0aW1lc3RhbXAiOjE3MTA5MTk1NzgsImtleSI6InVuaXB1cy1zc28ifQ.fHr55JJuJJyFpEIRfFf45q9Q8nWePNZLIsdD2LbVFEyn1bnkSb0aw4kWta-aoPIh83MPc_R0RU1kM8-LvvAt3o1Yz_bpyYYgdJ-L94dxYSqYY4twb43YxkQiaRIBotoilNvs3nnhBv5cFAVq6cyNAT-y5WzDYMFZxZcj-9P0WDblUVgCslT2vOaLEpxL54KA-woL3wGBCfBPvLr3Spo2HYUJ4V9AqwWEtQzSu93L-HhC8QoHHu-wwXBhdgGIq5bRqWpozcuay_4LjdSgl9BuuTOfAnqZ4SQE9oCNuI0SBeb8RUwo8RzIhFsRlYkR9NRWluAQWfOLAMzKlKOVP-MN1Q
     """
        lst = cookie_str.split("; ")
        dic = {}
        for it in lst:
            k, v = it.split("=", 1)
            dic[k.strip()] = v.strip()

        yield scrapy.Request(
            url=UPaSpider.start_urls[0],
            cookies=dic
        )

    def parse(self, response):
        url_li = response.xpath("//div[@class='course-content']/div/span[@class='hideurl']/text()").extract()
        name_li = response.xpath("//div[@class='course-content']/div/div[@class='my_course_text']/div/text()")

        for url in url_li:
            yield scrapy.Request(
                url=response.urljoin(url),
                callback=self.parse_detail
            )

    def parse_detail(self, response, **kwargs):
        url_homeworks = response.xpath("//a[@id='homeWrokNav']/@href").extract()

        url_tests = response.xpath("//a[@id='testNav']/@href").extract()
        for url_homework in url_homeworks:
            yield scrapy.Request(
                url=response.urljoin(url_homework),
                callback=self.parse_homework
            )
        for url_test in url_tests:
            yield scrapy.Request(
                url=response.urljoin(url_test),
                callback=self.parse_text
            )

    def parse_text(self, response, **kwargs):
        #print(response.text)
        pass

    def parse_homework(self, response, **kwargs):
        print(response.text)
