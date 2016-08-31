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
url_admin = 'https://administracion.uniandes.edu.co'
page = requests.get('https://administracion.uniandes.edu.co/index.php/es/facultad/sobre-la-facultad/eventos')
tree = html.fromstring(page.content)
eventos_p1 = tree.xpath('//div[@class="title"]//a')
link_principal = url_admin + eventos_p1[0].xpath('@href')[0]
i = 0
data = []
for evento in eventos_p1:
	if i > 0:
		link = url_admin + evento.xpath('@href')[0]
		d = parse_admin_evento(link)
		data.append(d)
		print "- - - - - - - - - - - - - - - - - - -"
		print "- - - - - - - - - - - - - - - - - - -"
	i=i+1
print data
with open('admin.json', 'w') as outfile:
	json.dump(data, outfile)
