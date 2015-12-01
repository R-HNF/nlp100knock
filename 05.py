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

#str
sentence_s="I am an NLPer"
#list
sentence_l=["I","am","an","NLPer"]


wgram,cgram=ngram(sentence_s,2)
print wgram
print cgram

wgram,cgram=ngram(sentence_l,2)
print wgram
print cgram
