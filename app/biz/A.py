#! /usr/bin/env python
# -*- coding:utf-8 -*-

from app.dao.A import ADao
class AService:

    def __init__(self):
        self.dao = ADao()

    def query(self, params):
        return self.dao.query(params)
        
