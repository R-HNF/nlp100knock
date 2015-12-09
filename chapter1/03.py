sentence="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words=sentence.split()
wordlen=[]
for w in words:
    if ("," in w) or ("." in w):
        wordlen.append(len(w)-1)
    else:
        wordlen.append(len(w))
print wordlen
