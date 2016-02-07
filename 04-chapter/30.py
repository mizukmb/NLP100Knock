# coding: utf-8

import mymodule as m

text = open("../data/neko.txt").read()

dict_list = []
for string in text.split():
    c_string = string.replace("　", "")
    dict_list.append(m.get_morphs(c_string))

