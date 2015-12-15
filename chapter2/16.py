#-*-coding:utf-8-*-
import sys
lines=list(open(sys.argv[1],'r'))
n=len(lines)/int(sys.argv[2])

for i in range(0,len(lines),n):
    for j in range(len(lines[i:i+n])):
        print lines[i:i+n][j].strip()
    print "-"*20

# shell command verification
# $split -l 8 hightemp.txt
