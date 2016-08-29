import scrapy

from tutorial.items import DmozItem
from tutorial.items import DependenciaItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["uniandes.edu.co"]
    start_urls = [
        "http://www.uniandes.edu.co/"
    ]

    def parse(self, response):
	#Submenus
	submenus = response.xpath('//ul[@class="dj-submenu2"]')
	submenu_facultades = submenus[4].xpath('li')
	submenu_deptos = submenus[5].xpath('li')
	lista_dependencias = submenu_facultades + submenu_deptos
        for dependencia in lista_dependencias:
		item = DependenciaItem()
		nombre = dependencia.xpath('a/text()').extract()[0]
		print "nombre "+ nombre
		link = dependencia.xpath('a/@href').extract()[0]
		print "link "+ link
		item['nombre'] = nombre
		item['link'] = link
		yield item
