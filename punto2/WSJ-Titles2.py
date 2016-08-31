import requests
import re
busqueda = "KKK"
urlopinion= 'http://www.wsj.com/xml/rss/3_7041.xml'
urlworldnews='http://www.wsj.com/xml/rss/3_7085.xml'
urlusbusiness='http://www.wsj.com/xml/rss/3_7014.xml'
values={'s':'basics','submit':'search'}
reqOpinion=requests.get(urlopinion)
reqWorldNews=requests.get(urlworldnews)
reqUsBusiness=requests.get(urlusbusiness)
respDataOpinion = reqOpinion.text
respDataWorldNews = reqWorldNews.text
respDataUsBusiness = reqUsBusiness.text
items_opinion = re.findall(r'<item>[\s\S]*?<\/item>',str(respDataOpinion))
items = []
for eachP in items_opinion:
	esta_en_titulo = re.findall(r'<title>(.*('+busqueda+').*)<\/title>',str(eachP))
	esta_en_descripcion = re.findall(r'<description>(.*('+busqueda+').*)<\/description>',str(eachP))
	if len(esta_en_titulo) > 0 or len(esta_en_descripcion) > 0:
		titulo = re.findall(r'<title>(.*?)<\/title>',str(eachP))
		items.append(titulo[0])
print items
#titlesWorldNews= re.findall(r'<title>(.*?)</title>',str(respDataWorldNews))
#for eachP in titlesWorldNews:
#	print(eachP)
#titlesUsBusiness= re.findall(r'<title>(.*?)</title>',str(respDataUsBusiness))
#for eachP in titlesUsBusiness:
#	print(eachP)
