#! /usr/bin/env python
# -*- coding:utf-8 -*-

from bottle import Bottle,view,redirect,request,response

from app.biz.A import AService

A = Bottle()

@A.get('/')
@view('A/index')
def A_index():
    aService = AService()
    name = aService.query('hizzgdev@163.com')
    return dict(message='module A in webapp template by', name=name)

