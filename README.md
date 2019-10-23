# amazon books scraping
In this example i scrap amazon books recor from amazon.in
for this i use python and google colab, google colab is a alternate version of jupyter notebook
in this i use google agents for contineous scrapping the files

Following are the steps you need to follow
 1)  install scrapy and scrapy agent
 pip install scrapy
 pip install scrapy-user-agents
 
 2) Then type following command to build scrapy project
 scrapy startproject amazon_scraping
 
 and movie to amazon_scraping folder using command cd amazon_scraping/
 
 3) then build spider using command
 scrapy genspider amazon_spider amazon.com
 
 4)Then do changes in item.py, setting.py and amazon_spider.py file
 
 5) run your program
 scrapy crawl amazon_spider
