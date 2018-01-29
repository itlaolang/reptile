import scrapy

class Ljdh(scrapy.Spider):
    name = "ljdh"
    start_urls=["http://www.lajitel.com"]
    def parse(self,response):
        print(response)
        for li in response.xpath('//*[@id="mailbody"]/div[2]/div[3]/ul/li'):

            #print("号码",li.xpath('.//div[1]/a/text()').extract ())
            print("类型", li.xpath('.//div[2]/text()').extract()[0])
            url="http://www.lajitel.com"+li.xpath('.//div[1] / a/@href').extract()[0]
            #print("详情", "http://www.lajitel.com"+li.xpath('.//div[1] / a/@href').extract()[0])
            yield scrapy.Request(url, callback=self.xiangqing)
            #print("归属地", li.xpath('.//div[1]/span[2]/text()').extract())
    def xiangqing(self,reponse):
        print("进来")
        print("号码",reponse.xpath('//*[@id="mailbody"]/div[1]/div[2]/div[2]/text()').extract()[0])
        print("归属地",reponse.xpath('//*[@id="mailbody"]/div[1]/div[2]/div[3]/ul/li[1]/text()').extract()[0])