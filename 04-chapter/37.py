# coding: utf-8

import mymodule as m
import matplotlib.pyplot as plt
from operator import itemgetter

text = open("../data/neko.txt").read()

dic = {}
for string in text.split():
    c_string = string.replace("　", "")
    for morph in m.get_morphs(c_string):
        if dic.has_key(morph["surface"])==False:
            dic[morph["surface"]] = 0
        dic[morph["surface"]] += 1

sorted_key = []
sorted_value = []
for d in sorted(dic.items(), key=itemgetter(1), reverse=True)[0:10]:
    sorted_key.append(d[0])
    sorted_value.append(d[1])

x = [1,2,3,4,5,6,7,8,9,10]
plt.bar(x, sorted_value, align="center")
plt.xticks(x)
# plt.show()
plt.savefig('./graph/37.png')
