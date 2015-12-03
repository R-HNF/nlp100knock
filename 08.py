#encryption/decryption function
def cipher(sentence):
    cip=""
    for c in sentence:
        if 'a'<=c and c<='z':
            cip+=chr(219-ord(c))
        else:
            cip+=c
    return cip

#original text
ori="Loading delayed either due to a recent crash or startup preferences."
print "original text"
print "\""+ori+"\"\n"

#cipher
enc=cipher(ori)
print "cipher"
print "\""+enc+"\"\n"

#decipher
dec=cipher(enc)
print "decipher"
print "\""+dec+"\""


