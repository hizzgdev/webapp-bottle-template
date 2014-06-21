#! /usr/bin/env python
# -*- coding=utf-8 -*-

try:
    from bottle import debug,run
except:
    import sys
    sys.path.append('_libs_')
    from bottle import debug,run

from app.web.root import root

if __name__ == '__main__':
    debug(True)
    run(app=root,host='0.0.0.0',reloader=True)
    #run(app=root,host='192.168.1.100',port='80')
    #run(server='gevent',app=root)
    #run(server='gevent',app=root,host='192.168.1.100',reloader=True)
