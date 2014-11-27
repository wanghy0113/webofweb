# -*- coding: utf-8 -*-

# Scrapy settings for MyCrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'MyCrawler'

SPIDER_MODULES = ['MyCrawler.spiders']
NEWSPIDER_MODULE = 'MyCrawler.spiders'
ITEM_PIPELINES = {
	'MyCrawler.pipelines.MycrawlerPipeline' : 800
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'MyCrawler (+http://www.yourdomain.com)'
