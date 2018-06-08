# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import json
from scrapy.linkextractors import LinkExtractor
'''
class ArtSpider(scrapy.Spider):
    name = "art"
    allowed_domains = ["images.so.com"]
    start_urls = ['http://images.so.com/']

    def parse(self, response):
        le=LinkExtractor(restrict_css='span.caption-text')
		#le.extract_links(response)

'''


class ImagesSpider(scrapy.Spider):
	BASE_URL='http://image.so.com/zj?ch=beauty&sn=%s&listtype=new&temp=1'#注意这里%S改过了
	#BASE_URL='http://image.so.com/j?q=%E9%BB%91%E4%B8%9D&src=srp&correct=%E9%BB%91%E4%B8%9D&pn=60&ch=&sn=%s&sid=fc52f43bfb771f78907396c3167f10ad&ran=0&ras=0&cn=0&gn=10&kn=50'
	start_index=0

	MAX_DOWNLOAD_NUM=1000
 
	name="images"
	start_urls=[BASE_URL %0]#??%0是干嘛的

	def parse(self,response):
		infos=json.loads(response.body.decode('utf-8'))
		for info in infos['list']:
			yield {'image_urls':[info['qhimg_url']]}

		self.start_index+=30
		if infos['count']>0 and self.start_index<self.MAX_DOWNLOAD_NUM:
			yield Request(self.BASE_URL % self.start_index)
'''
import json
r=response.body.decode('utf-8')
res=json.loads(r)
res
'''