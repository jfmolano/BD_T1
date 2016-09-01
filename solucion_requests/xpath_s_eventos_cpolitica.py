from lxml import html
import requests
import json

def parse_admin_evento(url):
	resp = {}
	page = requests.get(url)
	tree = html.fromstring(page.content)
	#Link evento	
	link = url
	print "URL: "+url
	resp['link'] = link
	#Nombre evento
	nombre = tree.xpath('//div[@class="event-detail-header"]/h2/text()')[0]
	print "Nombre: "+nombre
	resp['nombre'] = nombre
	#Fecha evento
	fecha = tree.xpath('//div[@class="event-detail-month"]/text()')[0] + " " + tree.xpath('//div[@class="event-detail-day"]/text()')[0]
	print "Fecha: "+fecha
	resp['fecha'] = fecha
	#Resumen evento
	contenido_div = tree.xpath('//div[@class="event-detail-description"]')[0]
	contenido = contenido_div.xpath('*[not (@class="pull-right")]//text()')
	contenido_str = ""
	for evento_d in contenido:
		contenido_str = contenido_str + evento_d
	resumen = contenido_str
	print "Resumen: "+resumen
	resp['resumen'] = resumen
	#Hora evento
	hora = tree.xpath('//*[contains(text(),"Hora:")]//text()')
	hora_str = ""
	if len(hora)>0:
		hora_str = hora[0].replace("Hora:","")
	print "Hora: "+hora_str
	resp['hora'] = hora_str
	#Lugar evento
	lugar = tree.xpath('//*[contains(text(),"Lugar:")]//text()')
	lugar_str = ""
	if len(lugar)>0:
		lugar_str = lugar[0].replace("Lugar:","")
	print "Lugar: "+lugar_str
	resp['lugar'] = lugar_str
	#No incluidos
	resp['nombre_e'] = ""
	resp['correo_e'] = ""
	resp['dependencia'] = "Facultad de Administracion"
	resp['palabras'] = ""
	return resp

#INICIO SCRIPT - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
url_eventos = 'https://facartes.uniandes.edu.co/index.php/eventos'
url_artes = 'https://facartes.uniandes.edu.co'
page = requests.get(url_eventos)
tree = html.fromstring(page.content)
eventos_p1 = tree.xpath('//ul[@class="ev_ul"]')
titulos = tree.xpath('//ul[@class="ev_ul"]//h2/text()')
hora_fecha = tree.xpath('//ul[@class="ev_ul"]//span[@class="hf_event"]/text()')
lugares = tree.xpath('//ul[@class="ev_ul"]//span[@class="lu_event"]/text()')
links = tree.xpath('//ul[@class="ev_ul"]//a[@class="ev_link_row"]/@href')
des = tree.xpath('//ul[@class="ev_ul"]//p/text()')
data = []
i = 0
j = 0
for evento in eventos_p1:
	nombre = titulos[i]
	hora_str = hora_fecha[i].string.split("|")[0]
	fecha = hora_fecha[i].string.split("|")[1]
	lugar_str = lugares[i]
	link = url_artes + links[i]
	if i == 0:
		j = 3
	if i == 1:
		j = 8
	if i == 2:
		j = 13
	if i == 3:
		j = 18
	resumen = des[j]
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
	resp['dependencia'] = "Facultad de Artes"
	resp['palabras'] = ""
	data.append(resp)
	print "- - - - - - - - - - - - - - - - - - -"
	print "- - - - - - - - - - - - - - - - - - -"
print data
with open('arte.json', 'w') as outfile:
	json.dump(data, outfile)
