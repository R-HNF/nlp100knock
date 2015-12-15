#-*-coding:utf-8-*-
import json

f = open('jawiki-country.json', 'r')

jsonData = json.load(f)

print json.dumps(jsonData)

f.close()
