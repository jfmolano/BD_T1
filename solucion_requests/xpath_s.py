from lxml import html
import requests
import json

page = requests.get('http://www.uniandes.edu.co/')
tree = html.fromstring(page.content)
submenus = tree.xpath('//ul[@class="dj-submenu2"]')
submenu_facultades= submenus[4].xpath('li')
submenu_deptos = submenus[5].xpath('li')
lista_dependencias = submenu_facultades + submenu_deptos
data = []
for dependencia in lista_dependencias:
	d = {}
	nombre = dependencia.xpath('a/text()')[0].encode('utf8')
        d['nombre'] = nombre
	print "nombre "+ nombre
	link = dependencia.xpath('a/@href')[0]
        d['link'] = link
	print "link "+ link
	data.append(d)
print data
with open('dependencias.json', 'w') as outfile:
	json.dump(data, outfile)
