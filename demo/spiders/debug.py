# coding:utf-8
# created by liNan

"""
调试
前两个参数是不变的，第三个参数请使用自己的spider的名字
"""
import sys

import os
from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy', 'crawl', 'wb'])
