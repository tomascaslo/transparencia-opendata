# -*- coding: utf-8 -*-

import pymongo
import random
import json
import pickle
import jsonpickle

MONGODB_URI = 'mongodb://tomascaslo:gastopublico@ds033489.mongolab.com:33489/gastopubliconl'

def main():
	client = pymongo.MongoClient(MONGODB_URI)
	
	db = client.get_default_database()

	data = db['2012']
	rand = random.randint(0, 3071)
	dato = data.find_one({'aid': rand})
	#dato = str(dato)
	#print dato
	#jsonobj = jsonpickle.encode(dato)

	datos = {}

	for k, v in dato.iteritems():
		print k
		datos[k] = str(v).encode("utf-8")

	print json.dumps(datos)
	print type(datos)
	#print str(rand) + ' ' + str(dato[('Línea').decode("utf-8")]) 

if __name__ == '__main__':
	main() 