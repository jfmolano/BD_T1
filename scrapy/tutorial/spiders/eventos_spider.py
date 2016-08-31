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
        "https://administracion.uniandes.edu.co/index.php/es/facultad/sobre-la-facultad/eventos/",
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
	print "URL: " + response.url
	#ADMINISTRACION
	if response.url == 'https://administracion.uniandes.edu.co/index.php/es/facultad/sobre-la-facultad/eventos/':
		print "Entra a " + response.url
		#yield parse_admin(self, response)
		yield scrapy.Request(response.url, callback=self.parse_admin)

#ADMINISTRACION /////////////////////////////////////////////////////////////////////////////////////////////////////
    def parse_admin(self, response):
	eventos_p1 = response.xpath('//div[@class="title"]//a')
	link_principal = response.urljoin(eventos_p1[0].xpath('@href')[0].extract())
	yield scrapy.Request(link_principal, callback=self.parse_admin_evento_principal)
	i = 0
        for evento in eventos_p1:
		if i > 0:
			link = response.urljoin(evento.xpath('@href')[0].extract())
			yield scrapy.Request(link, callback=self.parse_admin_evento)
		i=i+1

    def parse_admin_evento_principal(self, response):
	item = EventoItem()
	item['nombre'] = response.xpath('//h2[@class="itemTitle"]/text()')[0].extract()
	item['fecha'] = response.xpath('//h2[@class="itemTitle"]/text()')[0].extract()
	item['hora'] = response.xpath('//h2[@class="itemTitle"]/text()')[0].extract()
	item['lugar'] = response.xpath('//h2[@class="itemTitle"]/text()')[0].extract()
	item['nombre_e'] = response.xpath('//h2[@class="itemTitle"]/text()')[0].extract()
	item['correo_e'] = response.xpath('//h2[@class="itemTitle"]/text()')[0].extract()
	item['link'] = response.url
	item['resumen'] = response.xpath('//h2[@class="itemTitle"]/text()')[0].extract()
	item['palabras'] = response.xpath('//h2[@class="itemTitle"]/text()')[0].extract()
	yield item

    def parse_admin_evento(self, response):
	item = EventoItem()
	item['nombre'] = response.xpath('//div[@class="event-detail-header"]/h2/text()')[0].extract()
	item['fecha'] = response.xpath('//div[@class="event-detail-month"]/text()')[0].extract() + " " + response.xpath('//div[@class="event-detail-day"]/text()')[0].extract()
	contenido_div = response.xpath('//div[@class="event-detail-description"]')
	contenido = contenido_div.xpath('*[text() and not(@name="script")]//text()')
	contenido_str = ""
	for evento_d in contenido:
		contenido_str = contenido_str + evento_d.extract()
	hora = response.xpath('//*[contains(text(),"Hora:")]')[0].extract()
	hora_str = ""
	if hora
	item['hora'] = response.xpath('//*[contains(text(),"Hora:")]')[0].extract().replace("Hora:","")
	item['lugar'] = response.xpath('//*[contains(text(),"Lugar:")]')[0].extract().replace("Lugar:","")
	item['nombre_e'] = "-"
	item['correo_e'] = "-"
	item['link'] = response.url
	item['resumen'] = contenido_str
	item['palabras'] = "a"
	yield item
	#a.xpath('*[text() and not(@class="pull-right")]//text()')
	#a = response.xpath('//div[@class="event-detail-description"]')
#ADMINISTRACION ///////////////////////////////////////////////////////////////////////////////////////////////////// //*[contains(text(),"Hora")]
		
	
