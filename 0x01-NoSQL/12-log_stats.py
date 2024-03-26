#!/usr/bin/env python3

'''A Python module provides some stats about Nginx logs stored in MongoDB'''

from pymongo import MongoClient


if __name__ == '__main__':
    '''adding the top 10 of the most present IPs in the collection nginx of the database logs'''
    con = MongoClient('mongodb://localhost:27017')
    collection = con.logs.nginx

    print(f'{collection.estimated_document_count()} logs')

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print('Methods:')

    for req in methods:
        print('\tmethods {}: {}'.format(req,
              collection.count_documents({'method': req})))

    print('{} status check'.format(collection.count_documents(
          {'method': 'GET', 'path': '/status'})))
