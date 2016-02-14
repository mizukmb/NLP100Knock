# coding: utf-8

import mymodule as m
import sys

text = open("../data/neko.txt").read()

dict_list = []
for string in text.split():
    c_string = string.replace("　", "")
    list_tmp = []
    for morph in  m.get_morphs(c_string):
        if morph["pos"] == "名詞":
            list_tmp.append(morph["surface"])
        elif len(list_tmp) > 1:
            for w in list_tmp:
                sys.stdout.write(w)
            print ""
            list_tmp = []
        else:
            list_tmp = []

