# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import pymongo

import logging

#from scrapy import settings
#from scrapy.exceptions import DropItem
#import logging

class MongoDBPipeline(object):
    collection_name = 'MoteurRecherche1'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'my_research')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        dup_check =self.db[self.collection_name].find({'guid':item['guid'][0]}).count()
        if dup_check == 0 :     
            self.db[self.collection_name].insert(dict(item))
            logging.debug("document ajouté à mon MongoDB database!")
        else:
            logging.debug("document existe déjà!")     
        return item  
        