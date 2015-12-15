#-*-coding:utf-8-*-
file_col1=open("col1.txt",'r')
file_col2=open("col2.txt",'r')
file_col_12=open("col_12.txt",'w')

for c1,c2 in zip(file_col1,file_col2):
    file_col_12.write(c1.rstrip()+"\t"+c2.rstrip()+"\n")

file_col1.close()
file_col2.close()
file_col_12.close()

# shell command verification
# $ paste col1.txt col2.txt


