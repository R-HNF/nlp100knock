import random

#a blank before the period
sentence="I couldn't believe that I could actually understand what I was reading : the phenomenal of the human mind ."

def typoglycemia(sentence):
    #result words
    res=[]

    #get words
    words=sentence.split()

    for w in words:
        #the length of a word is less than four
        if len(w)<=4:
            res.append(w)
        #the length of a word is over than four
        else:
            #shuffle charcters
            ran=list(w[1:-1])
            random.shuffle(ran)
            
            #make shuffled word
            rw=w[0]+"".join(ran)+w[-1]
            res.append(rw)
        
    return " ".join(res)

print typoglycemia(sentence)
    
