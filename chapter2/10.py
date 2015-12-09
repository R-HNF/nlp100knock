#-*-coding:utf-8-*-
import sys
file=open(sys.argv[1],'r')
print len(list(file))
file.close()

# shell command verification
# $ wc hightemp.txt
