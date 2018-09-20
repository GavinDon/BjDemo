# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver


class WeiBoSpider(scrapy.Spider):
    # 配置环境变量无效，无奈只能在这写死
    # browser = webdriver.Chrome(executable_path="E:\python\python-3.7.0\Scripts\chromedriver")
    name = "wb"
    allowed_domains = ['m.weibo.cn']
    start_urls = ['https://m.weibo.cn/']

    def parse(self, response):
        print(response.text)