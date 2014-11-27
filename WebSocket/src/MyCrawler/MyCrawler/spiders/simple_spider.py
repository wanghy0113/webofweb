import scrapy

class SimpleSpider(scrapy.Spider):
  name = 'simplespider'
  allowed_domains = ['xioix.co']
  start_urls = ['http://www.xioix.co']
  
  def parse(self, response):
    self.log('content: %s ' % response.body)
