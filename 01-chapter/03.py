# coding: utf-8

w1 = u"パトカー"
w2 = u"タクシー"

print''.join([a + b for a, b in zip(w1, w2)]).encode('utf-8')
