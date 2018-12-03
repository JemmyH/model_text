# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from ..items import JobboleItem
from scrapy.utils.response import open_in_browser


class JobboleSpiderSpider(scrapy.Spider):
    name = 'jobbole_spider'
    allowed_domains = ['blog.jobbole.com', 'python.jobbole.com/']
    start_urls = ['http://python.jobbole.com/all-posts/']

    def parse(self, response):
        post_urls = response.xpath('/html/body/div[1]/div[3]/div//div[2]/p[1]/a[1]/@href').extract()
        for post_url in post_urls:
            print("here:", post_url)
            yield Request(url=post_url, callback=self.parse_detail, dont_filter=True)
        next_url = response.xpath("/html/body/div[1]/div[3]/div[21]/a/@href").extract()[-1]
        if next_url:
            yield Request(url=next_url, callback=self.parse, dont_filter=True)

    def parse_detail(self, response):
        item = JobboleItem()
        try:
            url = response.url
            title = response.xpath('body/div[1]/div[3]/div[1]/div[1]/h1/text()').extract()[0]
            public_time = response.xpath('body/div[1]/div[3]/div[1]/div[2]/p[1]/text()').extract()[0].strip().replace(
                ' ·', '')
            item_name = "->".join(response.xpath('body/div[1]/div[3]/div[1]/div[2]//a/text()').extract())
            introduction = response.xpath('body/div[1]/div[3]/div[1]/div[3]/p[1]/text()').extract()[0]
            article = response.xpath('body/div[1]/div[3]/div[1]/div[3]/article').extract()[0]
            item['url'] = url
            item['title'] = title
            item['public_time'] = public_time
            item['item_name'] = item_name
            item['introduction'] = introduction
            item['article'] = article
        except IndexError:
            url = response.url
            title = response.xpath('body/div[1]/div[3]/div[1]/div[1]/h1/text()').extract()[0]
            public_time = response.xpath('body/div[1]/div[3]/div[1]/div[2]/p[1]/text()').extract()[0].strip().replace(
                ' ·', '')
            item_name = "->".join(response.xpath('body/div[1]/div[3]/div[1]/div[2]//a/text()').extract())
            art_and_intro = response.xpath('body/div[1]/div[3]/div[1]/div[3]').extract()[0]
            article = "".join(art_and_intro)
            introduction = article.split("</p>")[0].replace("<p>", '')
            item['url'] = url
            item['title'] = title
            item['public_time'] = public_time
            item['item_name'] = item_name
            item['introduction'] = introduction
            item['article'] = article
        yield item
