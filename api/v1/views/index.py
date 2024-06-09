#!/usr/bin/python3
"""Status of your API"""

from flask import jsonify
from api.v1.views import app_views


@app_views.rout('/status')
def api_status()
""" status """
response = {'status' : 'ok'}
return jsonify(response)
