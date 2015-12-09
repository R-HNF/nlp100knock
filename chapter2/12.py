#-*-coding:utf-8-*-
import sys
file_t=open(sys.argv[1],'r')
file_col1=open("col1.txt",'w')
file_col2=open("col2.txt",'w')

for line in file_t:
    elements=line.split('\t')
    file_col1.write(elements[0]+"\n")
    file_col2.write(elements[1]+"\n")
    
file_t.close()
file_col1.close()
file_col2.close()


# shell command verification
# col1
# $ cut -f 1 hightemp.txt
# col2
# $ cut -f 2 hightemp.txt


