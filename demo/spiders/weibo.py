# -*- coding: utf-8 -*-
import requests
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from demo.items import WeiBoItem


class WeiBoSpider(scrapy.Spider):
    """"
    #配置环境变量无效，无奈只能在这设置executable_path
    最新版本selenium 不支持phantomJs
    官方建议使用chrome 或者 firefox 设置options 代替无头浏览器
    """

    name = "wb"
    page = 1
    browser = webdriver.Chrome(executable_path="E:\python\python-3.7.0\Scripts\chromedriver")
    chrome_options = Options()
    # 设置使用无头浏览器
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser.get('https://m.weibo.cn/')
    wait = WebDriverWait(browser, 10)
    start_urls = ['https://m.weibo.cn/']

    def parse(self, response):
        try:
            self.wait.until(
                ec.presence_of_element_located((By.CLASS_NAME, "m-search"))
            ).click()

            input_search = self.wait.until(ec.presence_of_element_located(
                (By.XPATH, "//*[@id='app']/div[1]/div[1]/div[1]/div/div/div[2]/form/input")))
            input_search.send_keys("电信")
            input_search.send_keys(Keys.ENTER)
            self.parse_paging()
        finally:
            self.browser.quit()
            pass

    """
    获取一页一页的数据
    """

    def parse_paging(self):
        req_value = self.browser.current_url
        req_url = f"https://m.weibo.cn/api/container/getIndex?{req_value.split('?')[1]}"
        print(req_url)
        resp = requests.get(req_url)
        # 获取到总页数
        if resp.status_code == 200:
            total_page = resp.json()['data']['cardlistInfo']['page_size']
            item = WeiBoItem()
            for page in range(int(total_page)):
                url = f"{req_url}&page={page+1}"
                resp = requests.get(url)
                resp_data = resp.json()
                for group in resp_data['data']['cards']:
                    for datail in group['card_group']:
                        if 'mblog' in datail:
                            item['page'] = page
                            item['tag'] = datail['mblog']['obj_ext']
                            item['title'] = datail['mblog']['page_info']['content1']
                            item['content'] = datail['mblog']['text']
                            item['update_time'] = datail['mblog']['created_at']

                # yield item