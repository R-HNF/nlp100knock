sentence="I am an NLPer"

def ngram(sentence,n):
    words=sentence.split()
    print [words[i:i+n] for i in range(0,len(words),n)]
    seq="".join(words)
    print [seq[i:i+n] for i in range(0,len(seq),n)]
    #print [sentence[i:i+n] for i in range(0,len(sentence),n)]

ngram(sentence,2)
