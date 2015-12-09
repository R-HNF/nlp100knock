#-*-encoding:utf-8-*-
import sys
lines=list(open(sys.argv[1],'r'))

n=int(sys.argv[2])

for line in lines[0:n]:
    print line.rstrip()

# shell command verification
# $ head -n 7 hightemp.txt
