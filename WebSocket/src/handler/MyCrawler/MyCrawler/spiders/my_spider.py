import scrapy 
import pika
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from tld import get_tld

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare('hello')

class MySpider(CrawlSpider):
  name = 'myspider'
  
  #urls = None
  def __init__(self, s_url=None, *args, **kwargs):
    self.start_urls = [s_url]
    self.rules = (Rule(LinkExtractor(allow_domains=(get_tld(s_url))),callback='parse_my_url', follow=True),)
    print get_tld(s_url)
    #self.allowed_domains = ['7ia7ia.com']
    super(MySpider, self).__init__(*args, **kwargs)
    
    
  #start_urls = urls
  #start_urls = ['http://www.7ia7ia.com']
  #rules = (Rule(LinkExtractor(allow_domains=('7ia7ia.com')),callback='parse_my_url', follow=True),)
  #allowed_domains = ['7ia7ia.com']


  def parse_my_url(self, response):
    channel.basic_publish(exchange='', routing_key='hello', body=response.url)
    
