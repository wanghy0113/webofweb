# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pika
from spiders import single_url_spider

_q_name = single_url_spider._queue_name

class MycrawlerPipeline(object):
    q_connection = None
    q_channel = None
    q_name = ""
    
    def __init__(self):
        self.q_connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.q_channel = self.q_connection.channel()
        self.q_name = _q_name
        print self.q_name
        self.q_channel.queue_declare(self.q_name)


    def process_item(self, item, spider):
        line = json.dumps(dict(item))
        self.q_channel.basic_publish(exchange='', routing_key=self.q_name, body=line)
        return item
