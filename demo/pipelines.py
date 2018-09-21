# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


""""
连接数据库存放数据
"""
import pymysql


class WeiBoPipeline(object):

    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='10.201.8.249',  # 数据库地址
            port=3306,  # 数据库端口
            db='spider',  # 数据库名
            user='root',  # 数据库用户名
            passwd='root',  # 数据库密码
            charset='utf8',  # 编码方式
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
        self.insertStatement = '''INSERT INTO  weibo (page,tag,title,content,update_time) VALUES (%s,%s,%s,%s,%s)'''
        self.deleterStatement = '''DELETE  FROM weibo'''

    def process_item(self, item, spider):
        self.cursor.execute(self.deleterStatement)
        self.cursor.execute(self.insertStatement, item['page']
                            , item['tag']
                            , item['title']
                            , item['content']
                            , item['update_time'] )
        self.connect.commit()
        return item

    def close_spider(self, spider):
        self.connect.close()