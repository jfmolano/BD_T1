# encoding=utf-8
import requests
from flask import Flask, jsonify, abort, make_response
import csv
import json
import io
import re

app = Flask(__name__)

marcas = [
    {
        'Id': u'1',
        'Dato': u'A'
    },
    {
        'Id': u'2',
        'Dato': u'B'
    }
]

@app.route('/api/marcas2', methods=['GET'])
def get_marcas2():
	return jsonify(marcas), 201

@app.route('/api/marcas', methods=['GET'])
def get_marcas():
	#json_data=open("../../scrapy/items.json", encoding='utf-8').read()
	with io.open("../../scrapy/items.json",'r',encoding='utf-8') as f:
    		json_data = f.read()
	print json_data
	json_data = unicode(json_data)
	#json_data = json_data.replace(r"""\u00f1""","ñ")
	#data = json.loads(json_data)
	return jsonify(json.loads(json_data)), 201

@app.route('/api/eventos', methods=['GET'])
def get_eventos():
	#json_data=open("../../scrapy/items.json", encoding='utf-8').read()
	with io.open("eventos.json",'r',encoding='utf-8') as f:
    		json_data = f.read()
	print json_data
	json_data = unicode(json_data)
	#json_data = json_data.replace(r"""\u00f1""","ñ")
	#data = json.loads(json_data)
	return jsonify(json.loads(json_data)), 201

@app.route('/api/rss/<A>', methods=['GET'])
def get_rss(A):
	busqueda = str(A)
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
		resp = {}
		esta_en_titulo = re.findall(r'<title>(.*('+busqueda+').*)<\/title>',str(eachP))
		esta_en_descripcion = re.findall(r'<description>(.*('+busqueda+').*)<\/description>',str(eachP))
		if len(esta_en_titulo) > 0 or len(esta_en_descripcion) > 0:
			titulo = re.findall(r'<title>(.*?)<\/title>',str(eachP))
			resp['titulo'] = titulo[0]
			items.append(resp)
	return jsonify(items), 201

@app.route('/api/suma', methods=['POST'])
def dar_suma_post():
	if not request.json or not 'A' in request.json:
		abort(400)
	A = int(request.json['A'])
	B = int(request.json.get('B', ""))
	marca = {
	'Resultado': (A+B)
	}
	return jsonify({'marca': marca}), 201

@app.route('/api/resta/<A>/<B>', methods=['GET'])
def dar_marca_get(A,B):
	marca = {
	'Resultado': (int(A)-int(B))
	}
	return jsonify({'marca': marca}), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
	app.run(host= '127.0.0.1')
