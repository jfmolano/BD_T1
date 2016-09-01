from lxml import html
import requests
import json

#INICIO SCRIPT - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
url_eventos = 'https://filosofia.uniandes.edu.co/index.php/noticias-y-eventos'
url_artes = 'https://filosofia.uniandes.edu.co'
page = requests.get(url_eventos)
tree = html.fromstring(page.content)
dias = tree.xpath('//div[@class="event"]//div[@class="day"]//text()')
meses = tree.xpath('//div[@class="event"]//div[@class="month"]//text()')
anios = tree.xpath('//div[@class="event"]//div[@class="year"]//text()')
palabras = tree.xpath('//div[@class="event"]//span[@class="cat"]//text()')
titulos = tree.xpath('//div[@class="event"]//a[not(@class="more")]//text()')
des = tree.xpath('//div[@class="event"]//span[@class="descshort"]//text()')
links = tree.xpath('//div[@class="event"]//a[@class="more"]/@href')
data = []
i = 0
for dia in dias:
	nombre = titulos[i]
	hora_str = ""
	fecha = dias[i] + " " + meses[i] + " " + anios[i]
	lugar_str = ""
	link = url_artes + links[i]
	resumen = des[i*2]
	#d = parse_admin_evento(link)
	#data.append(d)
	i = i+1
	resp = {}
	resp['link'] = link
	resp['nombre'] = nombre
	resp['fecha'] = fecha
	resp['resumen'] = resumen
	resp['hora'] = hora_str
	resp['lugar'] = lugar_str
	resp['nombre_e'] = ""
	resp['correo_e'] = ""
	resp['dependencia'] = "Departamento de Filosofia"
	resp['palabras'] = ""
	data.append(resp)
	print "- - - - - - - - - - - - - - - - - - -"
	print "- - - - - - - - - - - - - - - - - - -"
print data
with open('filosofia.json', 'w') as outfile:
	json.dump(data, outfile)
