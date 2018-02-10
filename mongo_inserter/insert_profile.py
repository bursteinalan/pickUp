#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 12:23:54 2017

@author: burstein
"""
import json
import dml
import prov.model

class user():
    def __init__(self):
        test=1
    def insert_user(self,new):
        client = dml.pymongo.MongoClient()
        repo = client.repo
        repo.authenticate('mongo_inserter', 'mongo_inserter')
        repo.pickup.users.insert(new)
 
        repo.logout()
        print(repo['pickup.users'].metadata())

    def new_user(self,location, age, name, gender):
        user={'location': location,
        'age':age,
        'name':name,
        'gender':gender}
        self.insert_user(user)


Alan= user()
Alan.new_user(' Boston',20,'Alan','M')