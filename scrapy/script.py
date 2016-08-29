import os
import time

while True:
	print "Ciclo de Scrapping"
	os.system('scrapy crawl dmoz -o items.json')
	time.sleep(10)
	os.system('rm items.json')
