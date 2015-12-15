#-*-coding:utf-8-*-
import sys
lines=list(open(sys.argv[1],'r'))
for p in dict([(k.split('\t')[0],1) for k in lines]).keys():
    print p 

# shell command verification

