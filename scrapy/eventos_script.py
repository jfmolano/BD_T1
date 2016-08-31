import os
import time

while True:
	print "Ciclo de Scrapping"
	os.system('clear')
	os.system('rm eventos.json')
	os.system('scrapy crawl eventos -o eventos.json')
	time.sleep(600)
