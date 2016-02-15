# coding: utf-8

import mymodule as m
from operator import itemgetter

text = open("../data/neko.txt").read()

dic = {}
for string in text.split():
    c_string = string.replace("　", "")
    for morph in m.get_morphs(c_string):
        if dic.has_key(morph["surface"])==False:
            dic[morph["surface"]] = 0
        dic[morph["surface"]] += 1

for d in sorted(dic.items(), key=itemgetter(1), reverse=True):
    print d[0], d[1]
    # k,v = d.items()
    # print k, v
