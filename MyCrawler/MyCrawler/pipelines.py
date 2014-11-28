# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pika


class MycrawlerPipeline(object):
    q_connection = None
    q_channel = None

    def __init__(self):
	    self.q_connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	    self.q_channel = self.q_connection.channel()
	    self.q_channel.queue_declare('hello')


    def process_item(self, item, spider):
        line = json.dumps(dict(item))
        self.q_channel.basic_publish(exchange='', routing_key='hello', body=line)
        return item
