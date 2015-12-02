#coding:utf-8
def tempreture(x,y,z):
    return u"%s時の%sは%s" % (x,y,z)

x=12
y=u"気温"
z=22.4
res=tempreture(x,y,z)

print res
