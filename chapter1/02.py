#-*-coding:utf-8-*-
str1=u"パトカー"
str2=u"タクシー"
print "".join([str1[i]+str2[i] for i in range(len(str1))])
