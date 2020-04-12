# -*- coding: utf-8 -*-
import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.tinydeal.com/specials.html']
    start_urls = ['http://www.tinydeal.com/specials.html/']

    def parse(self, response):
        pass
