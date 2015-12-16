#-*-coding:utf-8-*-
import re
import json

file_json=open("jawiki-country.json", 'r')
file_out=open("jawiki-england.txt",'w')
re_target=re.compile(u'イギリス')
for line in file_json:
    jsondata=json.loads(line)
    if re_target.search(jsondata['text']):
        file_out.write(jsondata['text'].encode('utf-8'))

file_json.close()
file_out.close()
