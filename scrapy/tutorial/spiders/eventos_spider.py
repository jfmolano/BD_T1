# encoding=utf-8
import scrapy
from unidecode import unidecode
from tutorial.items import DmozItem
from tutorial.items import DependenciaItem
from tutorial.items import EventoItem

class EventosSpider(scrapy.Spider):
    name = "eventos"
    allowed_domains = ["uniandes.edu.co"]
    start_urls = [
	"http://www.uniandes.edu.co/",
        "http://administracion.uniandes.edu.co",
	"http://arqdis.uniandes.edu.co/",
	"http://facartes.uniandes.edu.co/",
	"http://ciencias.uniandes.edu.co",
	"http://faciso.uniandes.edu.co/index.php?ac=inicio",
	"http://derecho.uniandes.edu.co/",
	"http://economia.uniandes.edu.co/",
	"http://cife.uniandes.edu.co/",
	"http://ingenieria.uniandes.edu.co/",
	"http://medicina.uniandes.edu.co/",
	"http://gobierno.uniandes.edu.co/",
	"http://cider.uniandes.edu.co/",
	"http://ceper.uniandes.edu.co/",
	"http://antropologia.uniandes.edu.co/",
	"http://arquitectura.uniandes.edu.co/scripts/p_intro.htm",
	"http://arte.uniandes.edu.co/",
	"http://c-politica.uniandes.edu.co/",
	"http://cienciasbiologicas.uniandes.edu.co/",
	"http://design.uniandes.edu.co/",
	"http://filosofia.uniandes.edu.co/",
	"http://fisica.uniandes.edu.co/",
	"http://geociencias.uniandes.edu.co/",
	"http://historia.uniandes.edu.co/",
	"http://humlit.uniandes.edu.co/",
	"http://ingbiomedica.uniandes.edu.co/",
	"http://civil.uniandes.edu.co/",
	"http://electrica.uniandes.edu.co/",
	"https://industrial.uniandes.edu.co/",
	"http://mecanica.uniandes.edu.co/",
	"http://ingquimica.uniandes.edu.co/",
	"http://sistemas.uniandes.edu.co/",
	"http://lenguas.uniandes.edu.co/",
	"http://matematicas.uniandes.edu.co/",
	"http://musica.uniandes.edu.co/",
	"http://psicologia.uniandes.edu.co/",
	"http://quimica.uniandes.edu.co/"
    ]

    def parse(self, response):
	#Submenus
	print "URL: " + response.url
	item = DependenciaItem()
	item['nombre'] = response.url
	item['link'] = response.url
	if response.url == 'http://www.uniandes.edu.co/':
		item['nombre'] = response.url + "ESTA"
		item['link'] = response.url + "ESTA"
		print "Entra"
	yield item