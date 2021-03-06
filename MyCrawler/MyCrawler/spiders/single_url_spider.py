import scrapy 
import pika
from scrapy.selector import HtmlXPathSelector
from tld import get_tld
from MyCrawler.items import url_node
from urlparse import urlparse, urljoin

print "*****************************\nstart crawling!"
_queue_name = ""
_max_node = 0;
_max_depth = 0;
class SingleUrlSpider(scrapy.Spider):
  name = 'single_url_spider'
  crawled_urls = set()
  #urls = None
  def __init__(self, s_url=None, uuid="default_queue", max_depth=0, max_node=0, *args, **kwargs):
    self.start_urls = [s_url]
    self.allowed_domains = [get_tld(s_url)]
    global _queue_name 
    _queue_name = uuid
    global _max_depth
    _max_depth = int(max_depth)
    global _max_node
    _max_node = int(max_node)
    print "crawl parameter: ", "max depth: ", _max_depth, "max node: ", _max_node
    
    #self.allowed_domains = ['7ia7ia.com']
    super(SingleUrlSpider, self).__init__(*args, **kwargs)
    
  #start_urls = urls
  #start_urls = ['http://www.7ia7ia.com']
  #rules = (Rule(LinkExtractor(allow_domains=('7ia7ia.com')),callback='parse_my_url', follow=True),)
  #allowed_domains = ['7ia7ia.com']
  def get_full_url(self, url, base_url):
    if url is not None:
      o = urlparse(url)
      if o.netloc is '':
        return urljoin(base_url, url)
      return url


  '''def parse(self, response):
    for sel in response.xpath('//a'):
      item = url_node()
      item['node_url'] = self.get_full_url(sel.xpath('@href').extract()[0], response.url)
      print item['node_url']
      item['parent_url'] = response.request.headers.get('Referer')
      item['node_depth'] = response.meta['depth']
      text = sel.xpath('text()').extract()[0]
      image_url = sel.xpath('image/@src').extract()
      item['element_dic'] = {'iamges':image_url, 'text':text,}
      yield item
      #if(item['node_url'] not in self.crawled_urls):
      #  self.crawled_urls.add(item['node_url'])
      yield scrapy.Request(item['node_url'],callback=self.parse)'''

  def parse(self, response):
    item = url_node()
    item['node_url'] = response.url
    item['node_parent'] = response.request.headers.get('Referer')
    item['node_depth'] = response.meta['depth']
    item['node_ele'] = {'image': response.request.headers.get('ele_image'), 
                        'text' : response.request.headers.get('ele_text'),}
    item['node_type'] = response.headers.get('Content-Type')
    self.crawled_urls.add(response.url)
    print "Current node number: ", len(self.crawled_urls)
    yield item
    if 'html' in response.headers.get('Content-Type') and response.meta['depth']<_max_depth:
      for sel in response.xpath('//a'):
        next_url = self.get_full_url(sel.xpath('@href').extract()[0], response.url)
        text = sel.xpath('text()').extract()
        image_url = sel.xpath('image/@src').extract()
        if len(image_url)>0:
          image_url = self.get_full_url(image_url[0], response.url)
        next_request_headers = {'ele_image':image_url, 'ele_text':text}
        next_request = scrapy.Request(next_url, callback=self.parse, headers=next_request_headers)
        #if(item['node_url'] not in self.crawled_urls):
        #  self.crawled_urls.add(item['node_url'])
        if len(self.crawled_urls) < _max_node:
          yield next_request
    
  