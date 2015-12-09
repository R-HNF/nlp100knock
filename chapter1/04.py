sentence="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
l=[1, 5, 6, 7, 8, 9, 15, 16, 19]
wordsloc={}
words=sentence.split()

for i in range(len(words)):
    if (i+1) in l:
        wordsloc.setdefault(words[i][0],0)
        wordsloc[words[i][0]]=i+1
    else:
        wordsloc.setdefault(words[i][0:2],0)
        wordsloc[words[i][0:2]]=i+1

print wordsloc
