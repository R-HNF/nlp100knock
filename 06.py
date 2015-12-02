def ngram(sentence,n):
    #change to str from list
    if(isinstance(sentence,list)):sentence=" ".join(sentence)

    #word n-gram
    words=sentence.split()
    wgram=[words[i:i+n] for i in range(len(words)-n+1)]

    #character n-gram
    cgram=[sentence[i:i+n] for i in range(len(sentence)-n+1)]
    #cgram=[[sentence[i+j] for j in range(n)] for i in range(len(sentence)-n+1)]
    #return n-grams
    return wgram,cgram



str1="paraparaparadise"
str2="paragraph"

wgram1,X=ngram(str1,2)
wgram2,Y=ngram(str2,2)
print "X=",X
print "Y=",Y,"\n"

ws=set(X)
print "(X+Y)=",ws.union(Y)
print "(X*Y)=",ws.intersection(Y)
print "(X-Y)=",ws.difference(Y)

print "(Y-X)=",set(Y).difference(X),"\n"


if "se" in X:
    print "'se' is in X"
else:
    print "'se' is not in X"

if "se" in Y:
    print "'se' is in Y"
else:
    print "'se' is not in Y"

