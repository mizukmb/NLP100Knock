# coding: utf-8

import mymodule as m

text = open("../data/neko.txt").read()

dict_list = []
for string in text.split():
    c_string = string.replace("　", "")
    for morph in m.get_morphs(c_string):
        if morph["pos"] == "動詞":
            print morph["base"]
            dict_list.append(morph["base"])


