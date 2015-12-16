#-*-coding:utf-8-*-
import re
import json

file_england=open("jawiki-england.txt", 'r')
file_out=open("jawiki-england-category.txt",'w')

re_target=re.compile(r'\[\[Category:.+\]\]')

for line in file_england:
    if re_target.match(line):
        file_out.write(line)
        
file_england.close()
file_out.close()
