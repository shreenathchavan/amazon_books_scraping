# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonScrapingItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    page_number = 2
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.in/s?k=books&ref=nb_sb_noss']

    def parse(self, response):
      
      items = AmazonScrapingItem()
      product_name = response.css('.a-color-base.a-text-normal::text').extract()
      product_author = response.css('.a-color-secondary .a-size-base+ .a-size-base , .index\=0 .a-text-price , .a-color-secondary .a-size-base.a-link-normal').css('::text').extract()
      product_price = response.css('.a-price-whole').css('::text').extract()
      product_imglink = response.css('.s-image::attr(src)').extract()  
      items['product_name'] = product_name
      items['product_author'] = product_author
      items['product_price'] = product_price
      items['product_imagelink'] = product_imglink
      yield items

      next_page = 'https://www.amazon.in/s?k=books&page='+ str(AmazonSpiderSpider.page_number)
      if AmazonSpiderSpider.page_number <= 20:
        AmazonSpiderSpider.page_number += 1
        yield response.follow(next_page, callback = self.parse, dont_filter=True)




      pass
  
