#-*-coding:utf-8-*-
import sys
lines=list(open(sys.argv[1],'r'))
wcount={}
for l in lines:
    w=l.split('\t')[0]
    wcount.setdefault(w,0)
    wcount[w]+=1

wcount_sorted=sorted(wcount.items(),key=lambda x:x[1],reverse=True)

for w,c in wcount_sorted:
    print w,c
    
# shell command verification
# $ cut -f 1 hightemp.txt|sort|uniq -c|sort -r
