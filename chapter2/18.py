#-*-coding:utf-8-*-
import sys
lines=list(open(sys.argv[1],'r'))

lines_splited=[l.split('\t') for l in lines]

lines_sorted=sorted(lines_splited,key=lambda x:x[2])

for l in lines_sorted:
    print '\t'.join(l).strip()

# shell command verification
# $ sort -k3 hightemp.txt
