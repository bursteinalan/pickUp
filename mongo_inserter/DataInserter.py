#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 12:23:54 2017

@author: burstein
"""
import json
import dml
import prov.model
class reader(dml.Algorithm):
    contributor = 'mongo_inserter'
    reads = []
    writes = ['yelp.reviews']
    @staticmethod
    def execute(trial = False):
        client = dml.pymongo.MongoClient()
        repo = client.repo
        repo.authenticate('mongo_inserter', 'mongo_inserter')
        
        repo.dropCollection("reviews")
        repo.createCollection("reviews")

        data=[{
        'test':'test'
        }]
        
        repo['pickup.users'].insert_many(data)
        repo['pickup.users'].metadata({'complete':True})
        repo.logout()
        print(repo['pickup.users'].metadata())
    @staticmethod
    def provenance(doc = prov.model.ProvDocument(), startTime = None, endTime = None):
        client = dml.pymongo.MongoClient()
        repo = client.repo
        return doc

reader.execute()