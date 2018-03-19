#!/usr/bin/env python

# App cliente recibe json por URL

import json
import requests

response = requests.get('http://localhost:8080/users')
data = response.json()
# Devuelve el primer nombre
print data['users'][0]['name']
