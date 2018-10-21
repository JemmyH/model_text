# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobboleItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()  # 文章URL
    title = scrapy.Field()  # 文章标题
    public_time = scrapy.Field()  # 发表时间
    item_name = scrapy.Field()  # 文章所属类别
    introduction = scrapy.Field()  # 文章简介
    article = scrapy.Field()  # 正文（建议将HTML标签也一起保存）
    favour_num = scrapy.Field()   # 点赞数
    collection_num = scrapy.Field()  # 收藏数
