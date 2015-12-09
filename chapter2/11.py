#-*-coding:utf-8-*-
import sys
file_t=open(sys.argv[1],'r')
file_b=open("hightemp_b.txt",'w')

for line in file_t:
    elements=line.split('\t')
    newline=' '.join(elements)
    file_b.write(newline)
    
file_t.close()
file_b.close()


# shell command verification
# $ sed s/$'\t'/' '/g hightemp.txt
