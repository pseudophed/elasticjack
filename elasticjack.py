#!/usr/bin/python3.4
# ElasticJack
# Tool for getting information from Elasticsearch.
# Written by Pseudophed Trismegistus (like a champ)
# Written in Python because Ruby is for pussies.

import json, sys, os, argparse, pycurl, io
from elasticsearch import Elasticsearch

'''
- Jack list of indexes available (DONE)
- Enumerate document counts for each index (DONE)
- Enumerate document count for specific index (DONE)
- Jack *x* documents for specific index
- Jack **all** documents for specific index
- Jack **all** documents for **all** indexes
'''

#global stuff
es = Elasticsearch('wa-elastic01:9200')

def getElasticInfo(returnDict=False):

	esInfo = es.info()
	
	if returnDict:
		return esInfo
	else:
		print('Elasticsearch Version: {}\nLucene Version: {}\nCluster Name: {}\nNode Name: {}'.format(esInfo['version']['number'], esInfo['version']['lucene_version'], esInfo['cluster_name'], esInfo['name']))
	
def getAllIndexes(hostname='wa-elastic01', port=9200, returnDict=False):
	
	#returnDict is a bool we set in case we want to use the output of the indexes in another function to feed in a list of indexes to work with
	#Set to False by default so we can easily print out indexes
	
	#Indexes is a dictionary with { "index_name" : doc_count }
	indexes = {}
	pc = pycurl.Curl()
	pcBuffer = io.BytesIO()
	
	pc.setopt(pc.URL, 'http://{}:{}/_cat/indices'.format(hostname, port))
	pc.setopt(pc.WRITEDATA, pcBuffer)
	
	#perform curl, catch exceptions if there are any
	try:
		pc.perform()
		tmpstring = pcBuffer.getvalue().decode('utf-8').split('\n')
		for line in tmpstring:
			if line != '':
				line = line.split(' ')
				#format for the curl output is as follows:
				#health status index   pri rep docs.count docs.deleted store.size pri.store.size
				#so we grab the field (space separated) at position 2 (index)
				
				#There will be a blank line at the end of the split, thus checks for this bullshit line
				if line[2]:
					#print(line)
					if line[5] == '':
						line[5] = 0
					indexes.update({line[2]:int(line[5])})

		pcBuffer.close()

	except Exception as e:
		print('Error: {}'.format(e))
		sys.exit(1)
	
	if returnDict:
		return indexes
	else:
		print('Available Indexes:')
		#print(indexes)
		for k,v in indexes.items():
			print('-> Index Name: {}, Documents: {}'.format(k, v))
			
def getSpecificIndexInfo(index, hostname='wa-elastic01', port=9200, returnCount = False):

	#returnCount is a bool we set in case we want to use the output of the index count in another function
	#Set to False by default so we can easily print out index count

	pc = pycurl.Curl()
	pcBuffer = io.BytesIO()
	
	#curl '<host>:<port>/<index>/_count'
	pc.setopt(pc.URL, 'http://{}:{}/{}/_count'.format(hostname, port, index))
	pc.setopt(pc.WRITEDATA, pcBuffer)
	
	#instantiate count
	count = 0
	
	#perform curl, catch exceptions if there are any
	try:
		pc.perform()
		jsonReturn = pcBuffer.getvalue().decode('utf-8')
		pcBuffer.close()
		
		jsonReturn = json.loads(jsonReturn)
		count = jsonReturn['count']

	except Exception as e:
		print('Error: {}'.format(e))
		sys.exit(1)
		
	if returnCount:
		return count
	else:
		print('Index: {}\nDocument Count: {}'.format(index, count))

def run():
	
	#getElasticInfo()
	#getAllIndexes()
	getSpecificIndexInfo(index='fail')
	sys.exit(0)

if __name__ == '__main__':	
	
	run()