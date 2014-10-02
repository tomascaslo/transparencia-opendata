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

	for i in range(3071):
		dato = data.update(
			{"aid":i}, 
			{"$set":
				{"Regular": 0, 
				"Sospechoso": 0, 
				"Irregular": 0}
			}
		)
		print "agregando dato " + str(i)

if __name__ == '__main__':
	main()