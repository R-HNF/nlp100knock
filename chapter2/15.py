#-*-coding:utf-8-*-
import sys
lines=list(open(sys.argv[1],'r'))

n=int(sys.argv[2])
start=len(lines)-n

for line in lines[start:start+n]:
    print line.rstrip()

# shell command verification
# $ tail -n 7 hightemp.txt
