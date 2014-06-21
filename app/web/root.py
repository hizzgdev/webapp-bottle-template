#! /usr/bin/env python
# -*- coding:utf-8 -*-

from bottle import Bottle,view,static_file,redirect,request,response
root = Bottle()

# you can mount any module like A below
from app.web.A import A
root.mount(A,'/a')

# route all static file request
@root.get('/static/:path#.*#')
def static_route(path):
    return static_file(path,root='static')

# route favicon.ico request
@root.get('/favicon.ico')
def favicon_route():
#   you can send to the static file
#   return static_route('favicon.ico')
#   or just return an empty string
    return ''

@root.get('/')
@view('index')
def root_index():
#   you may like to send redirect to the login page
#   redirect('/login')
    return dict(message='webapp template by hizzgdev@163.com')

