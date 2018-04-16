# -*- coding: utf-8 -*-
import platform
import psutil
import shutil
import json

from eve import Eve
from flask import Response as RS

settings = {
    'MONGO_HOST': 'localhost',
    'MONGO_PORT': 27017,
    'DOMAIN': {}
}

app = Eve(settings = settings)
#rs = RS() # always have problem in this deployment, put into each function

@app.route('/processor')
def processor():

    rs = RS()
    rs.headers["status"] = 200
    rs.headers["Content-Type"] = "application/json; charset=utf-8"
    
    info = {
        'processor' : platform.processor()
    }

    rs.data = json.dumps(info)
    return rs

@app.route('/system')
def os():

    rs = RS()
    rs.headers["status"] = 200
    rs.headers["Content-Type"] = "application/json; charset=utf-8"
    
    info = {
        'operating system' : platform.system()
    }

    rs.data = json.dumps(info)
    return rs

@app.route('/space')
def space():

    rs = RS()
    rs.headers["status"] = 200
    rs.headers["Content-Type"] = "application/json; charset=utf-8"
    
    space = shutil.disk_usage("/home/")
    
    info = {
        'total space' : space[0],
        'used space' : space[1],
    }

    rs.data = json.dumps(info)
    return rs

if __name__ == '__main__':
    app.run()
