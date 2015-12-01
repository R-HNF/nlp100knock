sentence="I am an NLPer"
#sentence=["I","am","an","NLPer"]

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


wgram,cgram=ngram(sentence,2)
#wgram,cgram=ngram(sentence,3)
print wgram
print cgram
